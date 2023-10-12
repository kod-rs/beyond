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
import { downloadIcon } from '@progress/kendo-svg-icons';
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
    color: string;
}

export type Building_Chart_Series = {
    categoryField: string;
    id: string;
    flexibility: number;
}

/* A React component that is using the Kendo UI library to render a pie chart and an area chart. */
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

    const downloadJSON =() => {
        console.log(flexOffers);

        const data = JSON.stringify(flexOffers);
        const blob = new Blob([data], { type: 'application/json' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'flexOffers.json'; // Specify the desired filename here
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    }

    /**
     * "If the buildings array is not empty, then for each building in the buildings array, if the building
     * is selected, then add the building to the dataArr array. If the flexOffers array is not empty, then
     * for each flexOffer in the flexOffers array, for each building in the flexOffer's building_info
     * array, if the building is in the dataArr array, then add the building's flexibility to the
     * flexibility property of the pieItem object in the dataArr array."
     * 
     * I'm not sure if this is the best way to do this, but it works.
     * 
     * I hope this helps someone else.
     */
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
                        let pieItem = dataArr.find((item) => item.id === info.building_id);
                        if (pieItem) {
                            pieItem.flexibility += Math.round(info.flexibility * 100) / 100;
                        }
                    })
                });
            }
            setPieData(dataArr);
        }
    }

    /**
     * It takes an array of Building_Area_Chart_Data objects, and for each Building_Area_Chart_Data object,
     * it takes an array of Building_Chart_Series objects, and for each Building_Chart_Series object, it
     * takes a string, and if that string is not in the DayCategories array, it adds a new
     * Building_Chart_Series object to the array of Building_Chart_Series objects.
     * @param {Building_Area_Chart_Data[]} chartAreaData - Building_Area_Chart_Data[]
     */
    const addEmptyHoursToBuildingsInfo = (chartAreaData: Building_Area_Chart_Data[]) => {
        chartAreaData.forEach((_building_data) => {
            let _data_series: Building_Chart_Series[] = [];
            DayCategories.forEach((categoryName) => {
                let serie_ = _building_data.series.find((ser) => ser.categoryField === categoryName);
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

    /**
     * If buildings and flexOffers are defined, then create a new array of Building_Area_Chart_Data,
     * and for each flexOffer, for each building_info, create a new Building_Chart_Series, and if the
     * building_name of the Building_Chart_Series is already in the array of Building_Area_Chart_Data,
     * then add the Building_Chart_Series to the array of Building_Chart_Series, otherwise add a new
     * Building_Area_Chart_Data to the array of Building_Area_Chart_Data, and then call the
     * addEmptyHoursToBuildingsInfo function with the array of Building_Area_Chart_Data, and then set
     * the areaData state to the array of Building_Area_Chart_Data.
     */
    const setAreaDataFromFlexOffers = () => {
        if (buildings) {
            if (flexOffers) {
                let chartAreaData: Building_Area_Chart_Data[] = [];
                flexOffers.forEach((offer) => {
                    offer.building_info.forEach((info) => {
                        let _serie_data: Building_Chart_Series = {
                            categoryField: new Date(info.start_time).getUTCHours().toString(),
                            flexibility: Math.round(info.flexibility * 100) / 100,
                            id: info.building_id
                        } as Building_Chart_Series;
                        let _building_name = buildings.find((building) => building.building_id === info.building_id)?.building_name;
                        let _area_Chart_Data = chartAreaData.find((_data) => _data.building_name === _building_name);
                        if (_area_Chart_Data) {
                            _area_Chart_Data.series.push(_serie_data);
                        } else {
                            chartAreaData.push({
                                building_name: _building_name,
                                series: [_serie_data] as Building_Chart_Series[],
                                color: getColorFromBuildingID(info.building_id)
                            } as Building_Area_Chart_Data);
                        }
                    });
                });
                addEmptyHoursToBuildingsInfo(chartAreaData);
                setAreaData(chartAreaData);
            }            
        }        
    }

    /**
     * If the building is selected, add the building name to the categories array.
     */
    const getCategoriesForPieAndBarChart = () => {
        let categories = [] as string[];
        buildings?.forEach((building) => {
            if (building.selected) {
                categories.push(building.building_name);
            }
        });
        setPieCategories(categories);
    }

    /* A function that returns color for specified building_id */
    const getColorFromBuildingID = (building_id: string) => {
        if (buildings) {
            var color = buildings.find(building => building.building_id === building_id)?.color;
            return color;
        }
        return '#89CFF0';
    }

    /* A React Hook. It is a function that lets you “hook into” React features. For example, useState
    is a Hook that lets you add React state to function components. We call it inside a function
    component to add some local state to it. React will preserve this state between re-renders. */
    useEffect(() => {
        if (flexOffers) {
            getCategoriesForPieAndBarChart();
            setPieDataFromFlexOffers();
            setAreaDataFromFlexOffers();
        }
    }, [flexOffers]);

    /**
     * It takes an object with a category property and returns that property
     * @param {any} e - The event object.
     */
    const labelContent = (e: any) => e.category;

    /* Rendering a pie chart. */
    const renderPieChartSeriesItem = (items: Building_Chart_Series[]) => {
        return <ChartSeriesItem
                    key={'pie'}
                    type="donut"
                    tooltip={{ visible: true, format: "{0} Wh" }}
                    data={items.map((item) => { 
                        return {
                            ...item, color: getColorFromBuildingID(item.id)
                        }
                    })}
                    field={'flexibility'}
                    categoryField={'categoryField'}
                    colorField="color"
                >
                </ChartSeriesItem>
    }

    /* Rendering a column chart series item. */
    const renderColumnChartSeriesItem = (items: Building_Chart_Series[]) => {
        return <ChartSeriesItem
                    key={'coll'}
                    type="column"
                    tooltip={{ visible: true, format: "{0} Wh" }}
                    data={items.map((item) => { 
                        return {
                            ...item, color: getColorFromBuildingID(item.id)
                        }
                    })}
                    field={'flexibility'}
                    categoryField={'categoryField'}
                    colorField="color" />
    }

    /* A function that returns a ChartSeriesItem component. */
    const renderAreaChartSeriesItem = (item: Building_Area_Chart_Data, index:number) => {
        return <ChartSeriesItem
                    key={index}
                    type="area"
                    tooltip={{ visible: true, format: "{0} Wh" }}
                    data={item.series}
                    field={'flexibility'}
                    categoryField={'categoryField'}
                    name={item.building_name}
                    color={item.color}
                />
    }

    return (
        <>
            <RowContainer>
                <PieGraphContainer>
                    <TitleContainer>Insights & Analytics</TitleContainer>
                    {
                        pieData &&
                        <Chart style={{ height: '80%', width: '80%' }}>
                            <ChartTitle text="Asstets flexibility" />
                            <ChartLegend position="bottom" orientation="horizontal" />
                            <ChartCategoryAxis>
                                    <ChartCategoryAxisItem
                                        categories={pieCategories ? pieCategories : []}
                                        startAngle={45}
                                        labels={{ format: "d", rotation: "auto" }}
                                    />
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
                    <CustomContainer>
                        {
                            areaData &&
                            <Chart style={{ height: 300, width: '95%' }}>
                                <ChartTitle text="Flexibility usage during the day" />
                                <ChartLegend position="bottom" orientation="horizontal" />
                                <ChartCategoryAxis>
                                    <ChartCategoryAxisItem
                                        categories={DayCategories}
                                        labels={{ format: "d", rotation: "auto" }}
                                    />
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
                    </CustomContainer>
                    <CustomContainer>
                        {
                            pieData &&
                            <Chart style={{ height: 300, width: '50%' }}>
                                <ChartTitle text="Overall flexibility usage" />
                                <ChartLegend position="top" orientation="horizontal" />
                                <ChartCategoryAxis>
                                        <ChartCategoryAxisItem
                                            categories={pieCategories ? pieCategories : []}
                                            startAngle={45}
                                            labels={{ format: "d", rotation: "auto" }}
                                        />
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

            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Download .JSON'}
                onClick={downloadJSON}
                svgIcon={downloadIcon}
                themeColor="inverse" />
            <Outlet />
        </>
    );

};

export default InsightAnalytics;
