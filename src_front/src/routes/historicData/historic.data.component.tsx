import { FloatingActionButton, FloatingActionButtonAlign, Button } from '@progress/kendo-react-buttons';
import { useDispatch, useSelector } from 'react-redux';
import { Outlet,useNavigate } from 'react-router-dom';
import { selectBuildingsHistoricData } from '../../store/historicData/historicData.selector';
import { ButtonsContainer, DatePickerContainer, GraphContainer, RowContainer } from './historic.data.styles';
import { DatePicker, DatePickerChangeEvent } from "@progress/kendo-react-dateinputs";
import { useEffect, useState } from 'react';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
import { selectCurrentUser } from '../../store/user/user.selector';
import { getHistoricDataStart } from '../../store/historicData/historicData.action';
import { 
    Chart,
    ChartSeries,
    ChartSeriesItem,
    ChartCategoryAxis,
    ChartCategoryAxisItem,
    ChartTitle,
    ChartLegend,
    LineStyle,
} from "@progress/kendo-react-charts";
import { Building_Info, TimeseriesData } from '../../store/historicData/historicData.types';
import { DayCategories, MonthCategories, PERIOD_TYPES, YearCategories } from './historic.data.types';



const HistoricData = () => {
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const buildingsHistory = useSelector(selectBuildingsHistoricData);
    const currentUser = useSelector(selectCurrentUser);
    const dispatch = useDispatch();
    const today= new Date();
    const navigate = useNavigate();
    const [selectedDate, setSelectedDate] = useState<Date>(today);
    const [categories, setCategories] = useState<string[]>([]);
    const [periodType, setPeriodType] = useState<PERIOD_TYPES>(PERIOD_TYPES.DAY);
    const [filteredData, setFilteredData] = useState<Building_Info[]>([]);

    useEffect(() => {
        if (buildings) {
            //get buildings historic data list from backend
            let filtered = buildings.filter((building) => {
                if (building.selected) {
                    return building;
                }
            });
            dispatch(getHistoricDataStart(filtered));
        }
    }, [buildings]);

    useEffect(() => {
        if (buildingsHistory) {
            defineCategories();
            filterDataForChart();
        }
    }, [buildingsHistory, periodType, selectedDate]);

    useEffect(() => {
        if (currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    const toFlexRequests=()=>{
        navigate("/flex");
    }

    const toBuildings=()=>{
        navigate("/buildings");
    }

    const onChangeSelectedDate = (event: DatePickerChangeEvent) => {
        if (event.value) {
            setSelectedDate(event.value);
        }
    }

    const renderChartSeriesItem = (item: Building_Info, idx:number) => {
        return <ChartSeriesItem
                    key={idx}
                    type="area"
                    tooltip={{ visible: true }}
                    data={item.energy_info.map((info) => { return info.value })}
                    name={item.building_id} />
    }

    const defineCategories = () => {
        switch (periodType) {
            case PERIOD_TYPES.DAY:
                setCategories(DayCategories);
                break;
            case PERIOD_TYPES.MONTH:
                setCategories(MonthCategories);
                break;
            case PERIOD_TYPES.YEAR:
                setCategories(YearCategories);
                break;
            default:
        }
    }

    const filterDataForChart = () => {
        let tmpData = [] as Building_Info[];
        buildingsHistory?.forEach((building_info) => {
            let buildingid = building_info.building_id;
            let data = filterBuildingInfoByPeriodType(building_info);
            
            tmpData.push({
                building_id: buildingid,
                energy_info: calculateAverages(data),
            });
        })
        setFilteredData(tmpData);
    }

    const filterBuildingInfoByPeriodType = (building_info: Building_Info) => {
        return building_info.energy_info.filter((timeseries) => {
            let _date = new Date(timeseries.timestamp);
            switch (periodType) {
                case PERIOD_TYPES.YEAR:
                    if (_date.getUTCFullYear() === selectedDate.getUTCFullYear()) {
                        return timeseries;
                    }
                    break;
                case PERIOD_TYPES.MONTH:
                    if (_date.getUTCMonth() === selectedDate.getUTCMonth() &&
                        _date.getUTCFullYear() === selectedDate.getUTCFullYear()) {
                        return timeseries;
                    }
                    break;
                case PERIOD_TYPES.DAY:
                    if (_date.getUTCDay() === selectedDate.getUTCDay() &&
                        _date.getUTCMonth() === selectedDate.getUTCMonth() &&
                        _date.getUTCFullYear() === selectedDate.getUTCFullYear()) {
                        return timeseries;
                    }
                    break;
                default:
            }
        });
    }

    const calculateAverages = (_data: TimeseriesData[]) => {
        let tmpData = [] as TimeseriesData[];
        if (_data.length > 0) {
            tmpData = calcPeriodAverageValuesPerUnit(_data, tmpData);
        }
        return tmpData;
    }

    const calcPeriodAverageValuesPerUnit = (_data: TimeseriesData[], tmpData: TimeseriesData[]) => {
        let startValue = 0;
        let endValue = 0;
        switch (periodType) {
            case PERIOD_TYPES.DAY:
                endValue = 24;
                break;
            case PERIOD_TYPES.MONTH:
                startValue = 1;
                endValue = 32;
                break;
            case PERIOD_TYPES.YEAR:
                startValue = 1;
                endValue = 13;
                break;
            default:
        }
        for (let i = startValue; i < endValue; i++) {
            let data_by_period = [] as TimeseriesData[];
            _data.forEach((timeseries) => {
                let timeSpan = getTimespanFromPeriodType(timeseries);
                if (timeSpan === i) {
                    data_by_period.push(timeseries);
                }
            });
            let avgDate = "";
            let avgVal = 0;
            if (data_by_period.length > 0) {
                avgDate = data_by_period[0].timestamp;
                data_by_period.forEach((timeseries) => {
                    avgVal += timeseries.value;
                });
                avgVal = avgVal / data_by_period.length;
            }
            tmpData.push({
                timestamp: avgDate,
                value: Math.round(avgVal * 100) / 100
            });
        }
        return tmpData;
    }

    const getTimespanFromPeriodType = (timeseries: TimeseriesData) => {
        let _date = new Date(timeseries.timestamp);
        let result = 0;
        switch (periodType) {
            case PERIOD_TYPES.DAY:
                result = _date.getUTCHours();
                break;
            case PERIOD_TYPES.MONTH:
                result = _date.getUTCDate();
                break;                
            case PERIOD_TYPES.YEAR:
                result = _date.getUTCMonth()+1;
                break; 
            default:
        }
        return result;
    }



    return (
        <>
            <RowContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={today} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    <Chart style={{ height: 350, width:'90%' }}>
                        <ChartTitle text="Buildings consumption historic data" />
                        <ChartLegend position="top" orientation="horizontal" />
                        <ChartCategoryAxis>
                            <ChartCategoryAxisItem categories={categories ? categories : []} startAngle={45} />
                        </ChartCategoryAxis>
                        <ChartSeries>
                            {
                                filteredData && filteredData.map((item, idx) => (
                                    renderChartSeriesItem(item, idx)
                                ))
                            }
                        </ChartSeries>
                    </Chart>

                    <ButtonsContainer>
                        <Button onClick={() => { setPeriodType(PERIOD_TYPES.DAY) }}>Day</Button>
                        <Button onClick={() => { setPeriodType(PERIOD_TYPES.MONTH) }}>Month</Button>
                        <Button onClick={() => { setPeriodType(PERIOD_TYPES.YEAR) }}>Year</Button>
                    </ButtonsContainer>
                </GraphContainer>
            </RowContainer>
            
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Activate VPP configuration'}
                onClick={toFlexRequests}
            />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Return to previous step'}
                onClick={toBuildings}
                themeColor="inverse"
            />
            <Outlet />
        </>
    );
};

export default HistoricData;




