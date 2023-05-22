import { FloatingActionButton, FloatingActionButtonAlign, Button } from '@progress/kendo-react-buttons';
import { useDispatch, useSelector } from 'react-redux';
import { Outlet,useNavigate } from 'react-router-dom';
import { selectBuildingsHistoricData, selectIsLoadingHistoricData } from '../../store/historicData/historicData.selector';
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
} from "@progress/kendo-react-charts";
import { Building_Info, TimeseriesData } from '../../store/historicData/historicData.types';
import { DayCategories, MonthCategories, PERIOD_TYPES, YearCategories } from './historic.data.types';
import { Loader } from '@progress/kendo-react-indicators';
import { SpinnerContainer } from '../general.routes.styles';



/* A React component that is using the Kendo UI Chart component to display a chart. */
const HistoricData = () => {
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const buildingsHistory = useSelector(selectBuildingsHistoricData);
    const currentUser = useSelector(selectCurrentUser);
    const isLoading = useSelector(selectIsLoadingHistoricData);
    const dispatch = useDispatch();
    const today= new Date();
    const navigate = useNavigate();
    const [selectedDate, setSelectedDate] = useState<Date>(today);
    const [categories, setCategories] = useState<string[]>([]);
    const [periodType, setPeriodType] = useState<PERIOD_TYPES>(PERIOD_TYPES.DAY);
    const [filteredData, setFilteredData] = useState<Building_Info[]>([]);

    /* A react hook that is called when the component is mounted. It is used to get the buildings historic
    data list from the backend. */
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

    /* A react hook that is called when the component is mounted. It is used to get the buildings
    historic
        data list from the backend. */
    useEffect(() => {
        if (buildingsHistory) {
            defineCategories();
            filterDataForChart();
        }
    }, [buildingsHistory, periodType, selectedDate]);

    /* Checking if the user is logged in. If not, it redirects to the login page. */
    useEffect(() => {
        if (currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    /**
     * When the user clicks the button, navigate to the /flex route.
     */
    const toFlexRequests=()=>{
        navigate("/flex");
    }

    /**
     * When the user clicks on the button, navigate to the buildings page.
     */
    const toBuildings=()=>{
        navigate("/buildings");
    }

    /**
     * OnChangeSelectedDate is a function that takes an event of type DatePickerChangeEvent and sets
     * SelectedDate with the value.
     * @param {DatePickerChangeEvent} event - DatePickerChangeEvent
     */
    const onChangeSelectedDate = (event: DatePickerChangeEvent) => {
        if (event.value) {
            setSelectedDate(event.value);
        }
    }

    /* A function that takes a Building_Info and an index and returns a ChartSeriesItem. */
    const renderChartSeriesItem = (item: Building_Info, idx:number) => {
        return <ChartSeriesItem
                    key={idx}
                    type="area"
                    tooltip={{ visible: true }}
                    data={item.energy_info.map((info) => { return info.value })}
                    name={item.building_id} />
    }

    /**
     * If the periodType is equal to PERIOD_TYPES.DAY, then set the categories to DayCategories, else
     * if the periodType is equal to PERIOD_TYPES.MONTH, then set the categories to MonthCategories,
     * else if the periodType is equal to PERIOD_TYPES.YEAR, then set the categories to YearCategories,
     * else do nothing.
     */
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

    /**
     * It takes an array of objects, and for each object in the array, it filters the object's data
     * based on a period type, then calculates the average of the filtered data, and then pushes the
     * object's id and the average data into a new array.
     */
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

    /**
     * It filters a list of objects by a date property, and returns the filtered list.
     * @param {Building_Info} building_info - Building_Info = {
     * @returns An array of objects that match the criteria.
     */
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

    /**
     * CalculateAverages takes an array of TimeseriesData objects and returns an array of
     * TimeseriesData objects.
     * @param {TimeseriesData[]} _data - TimeseriesData[] = [{
     * @returns An array of TimeseriesData objects.
     */
    const calculateAverages = (_data: TimeseriesData[]) => {
        let tmpData = [] as TimeseriesData[];
        if (_data.length > 0) {
            tmpData = calcPeriodAverageValuesPerUnit(_data, tmpData);
        }
        return tmpData;
    }

    /**
     * It takes an array of objects, and returns an array of objects.     
     * The function is called with an array of objects, and
     * @param {TimeseriesData[]} _data - TimeseriesData[] = [{timestamp: "2020-01-01T00:00:00.000Z",
     * value: 1}, {timestamp: "2020-01-01T01:00:00.000Z", value: 2}, {timestamp: "2020
     * @param {TimeseriesData[]} tmpData - TimeseriesData[] = [];
     * @returns An array of objects with the following structure:
     */
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

    /**
     * It takes a timestamp and returns a number based on the periodType.
     * @param {TimeseriesData} timeseries - TimeseriesData = {
     * @returns the result of the switch statement.
     */
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
                <SpinnerContainer>
                    {isLoading && <Loader size="large" type="converging-spinner" />}
                </SpinnerContainer>
                
                <DatePickerContainer>
                    <DatePicker defaultValue={today} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    <Chart style={{ height: 350, width:'90%' }}>
                        <ChartTitle text="Buildings consumption historical data" />
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
                disabled={isLoading}
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




