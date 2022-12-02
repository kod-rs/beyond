import { FloatingActionButton, FloatingActionButtonAlign } from '@progress/kendo-react-buttons';
import {
    Chart,
    ChartCategoryAxis,
    ChartCategoryAxisItem,
    ChartLegend,
    ChartSeries,
    ChartSeriesItem,
    ChartSeriesLabels,
    ChartTitle
}    from '@progress/kendo-react-charts';
import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { selectAlgorithmData } from '../../store/algorithm/algorithm.selector';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
import { DayCategories } from '../historicData/historic.data.types';
import { CustomContainer, GraphContainer, PieGraphContainer, RowContainer, TitleContainer } from './insight.analytics.styles';

export type Building_Area_Chart_Data = {
    building_name: string;
    series: Building_Chart_Series[];
}

export type Building_Chart_Series = {
    categoryField: string;
    id: string;
    flexibility: number;
}

const InsightAnalytics = () => {
    const flexOffers = useSelector(selectAlgorithmData);
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const [pieCategories, setPieCategories] = useState<string[]>([]);
    const [pieData, setPieData] = useState<Building_Chart_Series[]>([]);
    const [areaData, setAreaData] = useState<Building_Area_Chart_Data[]>([]);
    const navigate = useNavigate();

 

    const toFlex = () => {
        navigate("/flex");
    }

    const setPieDataFromFlexOffers = () => {
        let dataArr = [] as Building_Chart_Series[];
        if (buildings) {
            buildings.forEach((building) => {
                if (building.selected) {
                    dataArr.push({ id: building.building_id, categoryField: building.building_name, flexibility: 0 });
                }
                
            });

            if (flexOffers) {
                flexOffers?.forEach((offer) => {
                    offer.building_info.forEach((info) => {
                        let pieItem = dataArr.find((item) => item.id == info.building_id);
                        if (pieItem) {
                            pieItem.flexibility += info.flexibility;
                        }
                    })
                });
            }
            setPieData(dataArr);
        }
    }

    const addEmptyHoursToBuildingsInfo = (chartAreaData: Building_Area_Chart_Data[]) => {
        chartAreaData.forEach((_building_data) => {
            let _data_series: Building_Chart_Series[] = [];
            DayCategories.forEach((categoryName) => {
                let serie_ = _building_data.series.find((ser) => ser.categoryField == categoryName);
                if (serie_ === null || serie_ === undefined) {
                    _data_series.push({
                        categoryField: categoryName,
                        flexibility: 0,
                        id: '0',
                    });
                } else {
                    _data_series.push(serie_);
                }
            })
            _building_data.series = _data_series;
        });
    }

    const setAreaDataFromFlexOffers = () => {
        if (buildings) {
            if (flexOffers) {
                let chartAreaData: Building_Area_Chart_Data[] = [];
                flexOffers.forEach((offer) => {
                    offer.building_info.forEach((info) => {
                        let _serie_data: Building_Chart_Series = {
                            categoryField: new Date(info.start_time).getUTCHours().toString(),
                            flexibility: info.flexibility,
                            id: info.building_id
                        } as Building_Chart_Series;
                        let _building_name = buildings.find((building) => building.building_id == info.building_id)?.building_name;
                        let _area_Chart_Data = chartAreaData.find((_data) => _data.building_name === _building_name);
                        if (_area_Chart_Data) {
                            _area_Chart_Data.series.push(_serie_data);
                        } else {
                            chartAreaData.push({
                                building_name: _building_name,
                                series: [_serie_data] as Building_Chart_Series[]
                            } as Building_Area_Chart_Data);
                        }
                    });
                });
                addEmptyHoursToBuildingsInfo(chartAreaData);
                setAreaData(chartAreaData);
            }
            
        }
        
    }

    const getCategoriesForPieAndBarChart = () => {
        let categories = [] as string[];
        buildings?.forEach((building) => {
            if (building.selected) {
                categories.push(building.building_name);
            }
        });
        setPieCategories(categories);
    }

    useEffect(() => {
        if (flexOffers) {
            getCategoriesForPieAndBarChart();
            setPieDataFromFlexOffers();
            setAreaDataFromFlexOffers();
        }
    }, [flexOffers]);

    const labelContent = (e:any) => e.category;

    const renderPieChartSeriesItem = (items: Building_Chart_Series[]) => {
        return <ChartSeriesItem
                    key={'pie'}
                    type="donut"
                    tooltip={{ visible: true, format: "{0} kWh" }}
                    data={items}
                    field={'flexibility'}
                    categoryField={'categoryField'}
                    //name={'name'} 
                >
                    <ChartSeriesLabels
                        color="	#000033"
                        background="none"
                        content={labelContent}
                    />
                </ChartSeriesItem>
    }

    const renderColumnChartSeriesItem = (items: Building_Chart_Series[]) => {
        return <ChartSeriesItem
                    key={'coll'}
                    type="column"
                    tooltip={{ visible: true, format: "{0} kWh" }}
                    data={items}
                    field={'flexibility'}
                    categoryField={'categoryField'} />
    }

    const renderAreaChartSeriesItem = (item: Building_Area_Chart_Data,index:number) => {
        return <ChartSeriesItem
            key={index}
            type="area"
            tooltip={{ visible: true, format: "{0} kWh" }}
            data={item.series}
            field={'flexibility'}
            categoryField={'categoryField'}
            name={item.building_name} />
    }

    return (
        <>
            <RowContainer>
                <PieGraphContainer>
                    <TitleContainer>Insights & Analytics</TitleContainer>
                    {
                        pieData &&
                        <Chart style={{ height: '80%', width: '80%' }}>
                            <ChartTitle text="Buildings flexibility" />
                            <ChartLegend position="bottom" orientation="horizontal" />
                            <ChartCategoryAxis>
                                    <ChartCategoryAxisItem categories={pieCategories ? pieCategories : []} startAngle={45} />
                            </ChartCategoryAxis>
                            <ChartSeries>
                                {
                                    renderPieChartSeriesItem(pieData)
                                }
                            </ChartSeries>
                        </Chart>
                    }
                    
                </PieGraphContainer>
                <GraphContainer>
                    {
                        areaData &&
                        <Chart style={{ height: 300, width: '95%' }}>
                            <ChartTitle text="" />
                            <ChartLegend position="bottom" orientation="horizontal" />
                            <ChartCategoryAxis>
                                <ChartCategoryAxisItem categories={DayCategories} startAngle={45} />
                            </ChartCategoryAxis>
                            <ChartSeries>
                                {
                                    areaData && areaData.map((item, idx) => (
                                        renderAreaChartSeriesItem(item, idx)
                                    ))

                                }
                            </ChartSeries>
                        </Chart>
                    }
                    <CustomContainer>
                        {
                            pieData &&
                            <Chart style={{ height: 300, width: '50%' }}>
                                <ChartTitle text="Flexibility usage" />
                                <ChartLegend position="top" orientation="horizontal" />
                                <ChartCategoryAxis>
                                    <ChartCategoryAxisItem categories={pieCategories ? pieCategories : []} startAngle={45} />
                                </ChartCategoryAxis>
                                <ChartSeries>
                                    {
                                        renderColumnChartSeriesItem(pieData)
                                    }
                                </ChartSeries>
                            </Chart>
                        }
                    </CustomContainer>
                </GraphContainer>
            </RowContainer>
            
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Return to previous page'}
                onClick={toFlex}
                themeColor="inverse" />
            <Outlet />
        </>
    );

};

export default InsightAnalytics;