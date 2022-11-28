import { FloatingActionButton, FloatingActionButtonAlign, Button } from '@progress/kendo-react-buttons';
import { useDispatch, useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { DatePickerContainer, GraphContainer, RowContainer, SliderContainer } from './flex.requests.styles';
import { DatePicker, DatePickerChangeEvent } from "@progress/kendo-react-dateinputs";
import { Label } from '@progress/kendo-react-labels';
import { Slider, SliderChangeEvent } from "@progress/kendo-react-inputs";
import { useEffect, useState } from 'react';
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
import { DayCategories} from '../historicData/historic.data.types';
import { selectFlexDemand } from '../../store/flexDemand/flex.selector';
import { selectCurrentUser } from '../../store/user/user.selector';
import { getAlgorithmDataStart } from '../../store/algorithm/algorithm.action';
import { Algorithm_Request } from '../../store/algorithm/algorithm.types';
import { getFlexDemandStart } from '../../store/flexDemand/flex.action';


const FlexRequests = () => {
    const currentUser = useSelector(selectCurrentUser);
    const flexDemand = useSelector(selectFlexDemand);
    const dispatch = useDispatch();
    const today = new Date();
    const navigate = useNavigate();
    const [selectedDate, setSelectedDate] = useState<Date>();
    const [categories, setCategories] = useState<string[]>([]);

    const [filteredData, setFilteredData] = useState<Building_Info[]>([]);
    const [sliderPct, setSliderPct] = useState<number>(67);

    useEffect(() => {
        if (flexDemand) {
            defineCategories();
            getAlgorithmData();
        }
    }, [flexDemand]);

    useEffect(() => {
        if (selectedDate == null || selectedDate==undefined) {
            setSelectedDate(today);
        }
    }, []);

    useEffect(() => {
        if (selectedDate) {
            dispatch(getFlexDemandStart(selectedDate));
        }
    }, [selectedDate]);

    useEffect(() => {
        if (currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    const getAlgorithmData = () => {
        let algorithmRequest = {
            from: new Date(),
            to: new Date(),
            amount: sliderPct,
            building_energy_list: [],
        } as Algorithm_Request;
        dispatch(getAlgorithmDataStart(algorithmRequest));
    }

    const toInsightAnalytics = () => {
        navigate("/insight");
    }

    const toBuildings = () => {
        navigate("/buildings");
    }

    const onChangeSelectedDate = (event: DatePickerChangeEvent) => {
        if (event.value) {
            setSelectedDate(event.value);
            
        }
    }

    const renderChartSeriesItem = (item: Building_Info, idx: number) => {
        return <ChartSeriesItem
            key={idx}
            type="area"
            tooltip={{ visible: true }}
            data={item.energy_info.map((info) => { return info.value })}
            name={item.building_id} />
    }

    const renderChartCollumnSeriesItem = (item: Building_Info, idx: number) => {
        return <ChartSeriesItem
            key={idx}
            type="column"
            tooltip={{ visible: true }}
            data={item.energy_info.map((info) => { return info.value })}
            name={item.building_id} />
    }

    const defineCategories = () => {
        setCategories(DayCategories);
    }

 

    const onSubmit = () => {
        //TODO do submit
        return null;
    }

    const onSliderValueChange = (event: SliderChangeEvent) => {
        setSliderPct(Math.round(event.value * 10) / 10);
    }



    return (
        <>
            <RowContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={today} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    <Chart style={{ height: 300, width: '99%' }}>
                        <ChartTitle text="Flexibility requests" />
                        <ChartLegend position="top" orientation="horizontal" />
                        <ChartCategoryAxis>
                            <ChartCategoryAxisItem categories={categories ? categories : []} startAngle={45} />
                        </ChartCategoryAxis>
                        <ChartSeries>
                            {
                                filteredData && filteredData.map((item, idx) => (
                                    renderChartCollumnSeriesItem(item, idx)
                                ))
                            }
                        </ChartSeries>
                    </Chart>
                    <Chart style={{ height: 300, width: '99%' }}>
                        <ChartTitle text="Available VPP configuration" />
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
                    <SliderContainer>
                        <Label editorId="slider1">{sliderPct && (sliderPct + "%")}</Label>
                        <Slider id="slider1" min={0} max={100} step={1} defaultValue={67} onChange={onSliderValueChange} />
                    </SliderContainer>

                </GraphContainer>
                
            </RowContainer>

            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Insights & Analytics'}
                onClick={toInsightAnalytics} />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Go back to the building portfolio'}
                onClick={toBuildings}
                themeColor="inverse" />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "center" } as FloatingActionButtonAlign}
                text={'Submit'}
                onClick={onSubmit}
                themeColor="tertiary" />
            <Outlet />
        </>
    );

};

export default FlexRequests;