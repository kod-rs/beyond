import { FloatingActionButton, FloatingActionButtonAlign, Button } from '@progress/kendo-react-buttons';
import { useDispatch, useSelector } from 'react-redux';
import { Outlet,useNavigate } from 'react-router-dom';
import { selectBuildingsHistoricData } from '../../store/historicData/historicData.selector';
import { ButtonsContainer, DatePickerContainer, GraphContainer, RowContainer } from './historic.data.styles';
import { DatePicker, DatePickerChangeEvent } from "@progress/kendo-react-dateinputs";
import { useEffect, useState } from 'react';
import { selectBuildingsForCurrentUser } from '../../store/buildings/buildings.selector';
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


const HistoricData = () => {
    const buildings = useSelector(selectBuildingsForCurrentUser);
    const buildingsHistory = useSelector(selectBuildingsHistoricData);
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
    }, [buildingsHistory,periodType,selectedDate]);

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
                    name={item.building_id}
                />
    }

    const defineCategories = () => {
        switch (periodType) {
            case PERIOD_TYPES.DAY:
                setCategories(DayCategories);
                break;
            case PERIOD_TYPES.MONTH:
                setCategories(MonthCategories);
                break;
            case PERIOD_TYPES.MONTH:
                setCategories(YearCategories);
                break;
            default:
        }
    }

    const filterDataForChart = () => {
        let tmpData = [] as Building_Info[];
        buildingsHistory?.forEach((building_info) => {
            let buildingid = building_info.building_id;
            let data = building_info.energy_info.filter((timeseries) => {
                let _date = new Date(timeseries.timestamp);
                switch (periodType) {
                    case PERIOD_TYPES.YEAR:
                        if (_date.getFullYear() === selectedDate.getFullYear()) {
                            return timeseries;
                        }
                        break;
                    case PERIOD_TYPES.MONTH:
                        if (_date.getMonth() === selectedDate.getMonth() &&
                            _date.getFullYear() === selectedDate.getFullYear()) {
                            return timeseries;
                        }
                        break;
                    case PERIOD_TYPES.DAY:
                        if (_date.getDay() === selectedDate.getDay() &&
                            _date.getMonth() === selectedDate.getMonth() &&
                            _date.getFullYear() === selectedDate.getFullYear()) {
                            return timeseries;
                        }
                        break;
                    default:
                }
            });
            
            tmpData.push({
                building_id: buildingid,
                energy_info: calculateAverages(data),
            });
        })
        setFilteredData(tmpData);
    }

    const calculateAverages = (_data: TimeseriesData[]) => {
        switch (periodType) {
            case PERIOD_TYPES.YEAR:
                
                break;
            case PERIOD_TYPES.MONTH:
                
                break;
            case PERIOD_TYPES.DAY:

                break;
            default:
        }
        
        return _data;
    }

    return (
        <>
            <RowContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={today} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    <Chart style={{ height: 350, width:'90%' }}>
                        <ChartTitle text="Area Chart" />
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
                text={'Continue'}
                onClick={toFlexRequests}
            />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Back to Buildings'}
                onClick={toBuildings}
            />
            <Outlet />
        </>
    );
};

export default HistoricData;




