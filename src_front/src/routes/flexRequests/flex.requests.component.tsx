import { FloatingActionButton, FloatingActionButtonAlign, Button } from '@progress/kendo-react-buttons';
import { useDispatch, useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { CustomContainer, DatePickerContainer, GraphContainer, RowContainer, SliderContainer } from './flex.requests.styles';
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

import { Flex_Demand } from '../../store/flexDemand/flex.types';
import { selectFlexDate, selectFlexDemand } from '../../store/flexDemand/flex.selector';
import { selectCurrentUser } from '../../store/user/user.selector';
import { getAlgorithmDataStart, sendFlexOfferStart } from '../../store/algorithm/algorithm.action';
import { Algorithm_Request, Flex_Offer, Algorithm_Response } from '../../store/algorithm/algorithm.types';
import { getFlexDemandStart, setFlexDateStart } from '../../store/flexDemand/flex.action';
import { selectBuildingsHistoricData } from '../../store/historicData/historicData.selector';
import { selectAlgorithmData } from '../../store/algorithm/algorithm.selector';

export type Filtered_Flex_Data = {
    start_time: string,
    end_time: string,
    flexibility: number,
    categoryField: string,
}

const FlexRequests = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildingsHistory = useSelector(selectBuildingsHistoricData);
    const flexOffers = useSelector(selectAlgorithmData);
    const flexDemand = useSelector(selectFlexDemand);
    const flexDate = useSelector(selectFlexDate);
    const dispatch = useDispatch();
    const tomorrow = new Date(new Date().setDate(new Date().getDate()+1));
    const navigate = useNavigate();
    const [selectedDate, setSelectedDate] = useState<Date>();
    const [categories, setCategories] = useState<string[]>([]);
    const [filteredFlexDemandData, setFilteredFlexDemandData] = useState<Filtered_Flex_Data[]>([]);
    const [filteredFlexOfferData, setFilteredFlexOfferData] = useState<Filtered_Flex_Data[]>([]);
    const [sliderPct, setSliderPct] = useState<number>(100);

    useEffect(() => {
        if (flexDemand) {
            defineCategories();
        }
    }, [flexDemand]);

    useEffect(() => {
        if (selectedDate == null || selectedDate == undefined) {
            if (flexDate == null) {
                setSelectedDate(tomorrow);
            } else {
                setSelectedDate(flexDate);
            }
        }
    }, []);

    useEffect(() => {
        if (categories) {
            if (flexDemand) {
                setFilteredFlexDataFromDemand();
                getAlgorithmData();
            }
        }
    }, [categories,flexDemand]);

    useEffect(() => {
        if (selectedDate) {
            if (selectedDate !== flexDate) {
                dispatch(setFlexDateStart(selectedDate));
                dispatch(getFlexDemandStart(selectedDate));
            }
        }
    }, [selectedDate]);

    useEffect(() => {
        if (currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    useEffect(() => {
        if (flexOffers) {
            setFilteredFlexDataFromOffers();
        }
    }, [flexOffers]);

    const getTooltipForDemand = (demand: Flex_Demand) => {
        let start = new Date(demand.start_time);
        let end = new Date(demand.end_time);
        return start.toTimeString().split(' ')[0] + " - " + end.toTimeString().split(' ')[0];
    }

    const setFilteredFlexDataFromDemand = () => {
        if (flexDemand) {
            let data: Filtered_Flex_Data[] = flexDemand.map((demand) => {
                demand.flexibility = Math.round(demand.flexibility * 100) / 100;
                return { ...demand, categoryField: getTooltipForDemand(demand) }
            }) as Filtered_Flex_Data[];
            if (data) {
                setFilteredFlexDemandData(data);
            }
        }
    }

    const getTooltipForOffer = (offer: Flex_Offer) => {
        let start = new Date(offer.start_time);
        let end = new Date(offer.end_time);
        return start.toTimeString().split(' ')[0] + " - " + end.toTimeString().split(' ')[0];
    }

    const setFilteredFlexDataFromOffers = () => {
        if (flexOffers) {
            let data: Filtered_Flex_Data[] = flexOffers.map((offer) => {
                offer.offered_flexibility = Math.round(offer.offered_flexibility * 100) / 100;
                return { start_time:offer.start_time,end_time:offer.end_time,flexibility:offer.offered_flexibility, categoryField: getTooltipForOffer(offer) }
            }) as Filtered_Flex_Data[];
            if (data) {
                setFilteredFlexOfferData(data);
            }
        }
    }

    const setAlgorithmRequest = () => {
        let _tmp_flexDemand = JSON.parse(JSON.stringify(flexDemand)) as Flex_Demand[];
        let algorithmRequest = {
            flexibility_demands: _tmp_flexDemand?.map((demand) => {
                demand.flexibility = demand.flexibility * sliderPct / 100;
                return demand;
            }),
            building_energy_list: buildingsHistory,
        } as Algorithm_Request;
        return algorithmRequest;
    }

    const getAlgorithmData = () => {
        let algorithmRequest = setAlgorithmRequest();
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

    const defineCategories = () => {
        if (flexDemand) {
            let ctgs = flexDemand.map((demand) => {
                return getTooltipForDemand(demand)
            })
            if (ctgs) {
                setCategories(ctgs);
            }
        }
    }

    const onSubmit = () => {
        if (currentUser) {
            let algorithmResponse = {
                type: "algorithm_response",
                status: true,
                offers: flexOffers,
            } as Algorithm_Response;
            dispatch(sendFlexOfferStart(currentUser.user_id, algorithmResponse));
        }
    }

    const onSliderValueChange = (event: SliderChangeEvent) => {
        setSliderPct(Math.round(event.value * 10) / 10);
    }

    const renderBarChartSeriesItem = (items: Filtered_Flex_Data[],color?:string) => {
        return <ChartSeriesItem
                    key={'demand'}
                    type="column"
                    tooltip={{ visible: true, format: "{0} kWh" }}
                    data={items}
                    field={'flexibility'}
                    categoryField={'categoryField'}
                    color={color ? color : '#CC00FF'}/>
    }

    const onButtonReloadClick = () => {
        getAlgorithmData();
    }

    return (
        <>
            <RowContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={tomorrow} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    {
                        filteredFlexDemandData &&
                        <Chart style={{ height: 250, width: '99%' }} pannable={{ lock: "y" }} zoomable={{ mousewheel: { lock: "y" } }}>
                            <ChartTitle text="Flexibility requests" />
                            <ChartLegend position="top" orientation="horizontal" />
                            <ChartCategoryAxis>
                                <ChartCategoryAxisItem startAngle={45} categories={categories} />
                            </ChartCategoryAxis>
                            <ChartSeries>
                                {
                                    renderBarChartSeriesItem(filteredFlexDemandData)
                                }
                            </ChartSeries>
                        </Chart>
                    }
                    {
                        filteredFlexOfferData &&
                        <Chart style={{ height: 250, width: '99%' }}>
                            <ChartTitle text="Available VPP configuration" />
                            <ChartLegend position="top" orientation="horizontal" />
                            <ChartCategoryAxis>
                                <ChartCategoryAxisItem categories={categories ? categories : []} startAngle={45} />
                            </ChartCategoryAxis>
                            <ChartSeries>
                                {
                                    renderBarChartSeriesItem(filteredFlexOfferData,"green")
                                }
                            </ChartSeries>
                        </Chart>
                    }
                    <CustomContainer>
                        <SliderContainer>
                            <Label editorId="slider1">{sliderPct + "%"}</Label>
                            <Slider id="slider1" min={0} max={100} step={1} defaultValue={sliderPct} onChange={onSliderValueChange} />
                            <Button onClick={onButtonReloadClick} themeColor="tertiary" style={{margin:'5px'}}>Reload VPP configuration</Button>
                        </SliderContainer>
                        
                    </CustomContainer>
                </GraphContainer>
                
            </RowContainer>

            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "center" } as FloatingActionButtonAlign}
                text={'Insights & Analytics'}
                onClick={toInsightAnalytics} />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Go back to the building portfolio'}
                onClick={toBuildings}
                themeColor="inverse" />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Submit'}
                disabled={(currentUser===null) || (flexOffers===undefined)}
                onClick={onSubmit}
                themeColor="tertiary" />
            <Outlet />
        </>
    );

};

export default FlexRequests;