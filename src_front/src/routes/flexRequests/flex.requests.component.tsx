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
import { selectFlexDate, selectFlexDemand, selectFlexIsLoading } from '../../store/flexDemand/flex.selector';
import { selectCurrentUser } from '../../store/user/user.selector';
import { getAlgorithmDataStart, sendFlexOfferStart } from '../../store/algorithm/algorithm.action';
import { Algorithm_Request, Flex_Offer, Algorithm_Response } from '../../store/algorithm/algorithm.types';
import { getFlexDemandStart, setFlexDateStart } from '../../store/flexDemand/flex.action';
import { selectBuildingsHistoricData } from '../../store/historicData/historicData.selector';
import { selectAlgorithmData, selectAlgorithmDataLoading, selectFlexOfferResponse } from '../../store/algorithm/algorithm.selector';
import { SpinnerContainer } from '../general.routes.styles';
import { Loader } from '@progress/kendo-react-indicators';
import {
    Notification,
    NotificationGroup,
} from "@progress/kendo-react-notification";
import { Fade } from "@progress/kendo-react-animation";

/**
 * Filtered_Flex_Data is an object with four properties: start_time, end_time, flexibility, and
 * categoryField. All of these properties are strings except for flexibility, which is a number.
 * @property {string} start_time - The start time of the flex data
 * @property {string} end_time - string,
 * @property {number} flexibility - number,
 * @property {string} categoryField - This is the name of the category.
 * @property {number} percentage - number,
 */
export type Filtered_Flex_Data = {
    start_time: string,
    end_time: string,
    flexibility: number,
    categoryField: string,
    percentage:number,
}

/* The above code is a React component that is using the Kendo UI library. */
const FlexRequests = () => {
    const currentUser = useSelector(selectCurrentUser);
    const buildingsHistory = useSelector(selectBuildingsHistoricData);
    const flexOffers = useSelector(selectAlgorithmData);
    const flexDemand = useSelector(selectFlexDemand);
    const flexDate = useSelector(selectFlexDate);
    const offerResponse = useSelector(selectFlexOfferResponse);
    const algorithmIsLoading = useSelector(selectAlgorithmDataLoading); 
    const flexDemandIsLoading = useSelector(selectFlexIsLoading); 
    const dispatch = useDispatch();
    const tomorrow = new Date(new Date().setDate(new Date().getDate()+1));
    const navigate = useNavigate();
    const [selectedDate, setSelectedDate] = useState<Date>();
    const [categories, setCategories] = useState<string[]>([]);
    const [filteredFlexDemandData, setFilteredFlexDemandData] = useState<Filtered_Flex_Data[]>([]);
    const [filteredFlexOfferData, setFilteredFlexOfferData] = useState<Filtered_Flex_Data[]>([]);
    const [showKWH, setShowKWH] = useState<boolean>(true);
    const [sliderPct, setSliderPct] = useState<number>(100);
    const [success, setSuccess] = useState<boolean|null>(null);
    const [error, setError] = useState<boolean | null>(null);

    /* A React Hook. It is a function that lets you “hook into” React features. For example, useState
    is a Hook that lets you add React state to function components. */
    useEffect(() => {
        if (flexDemand) {
            defineCategories();
        }
    }, [flexDemand]);

    /* Setting the selectedDate to tomorrow if the selectedDate is null or undefined. */
    useEffect(() => {
        if (selectedDate == null || selectedDate === undefined) {
            if (flexDate == null) {
                setSelectedDate(tomorrow);
            } else {
                setSelectedDate(flexDate);
            }
        }
    }, []);

    /* Checking if categories and flexDemand are not null, then it is calling the
    setFilteredFlexDataFromDemand() function. */
    useEffect(() => {
        if (categories) {
            if (flexDemand) {
                setFilteredFlexDataFromDemand();
            }
        }
    }, [categories,flexDemand]);

    /* Checking if the selectedDate is not equal to flexDate, then it will dispatch the
    setFlexDateStart and getFlexDemandStart. */
    useEffect(() => {
        if (selectedDate) {
            if (selectedDate !== flexDate) {
                dispatch(setFlexDateStart(selectedDate));
                dispatch(getFlexDemandStart(selectedDate));
            }
        }
    }, [selectedDate]);

    /* Checking if the currentUser is null or undefined, if it is, it will navigate to the auth page. */
    useEffect(() => {
        if (currentUser === null || currentUser === undefined) {
            navigate("/auth");
        }
    }, [currentUser]);

    /* Checking if flexOffers is true, if it is, it will set the filteredFlexDataFromOffers. */
    useEffect(() => {
        if (flexOffers) {
            setFilteredFlexDataFromOffers();
        }
    }, [flexOffers]);

    /* Checking if the offerResponse is true, if it is, it will set the success to the status of the
    offerResponse. If it is not true, it will set the error to the opposite of the status of the
    offerResponse. */
    useEffect(() => {
        if (offerResponse) {
            setSuccess(offerResponse.status);
            setError(!offerResponse.status);
        }
    }, [offerResponse]);

    /**
     * "getTooltipForDemand" is a function that takes a "demand" object as an argument and returns a
     * string.
     * @param {Flex_Demand} demand - Flex_Demand
     * @returns A function that takes a demand object and returns a string.
     */
    const getTooltipForDemand = (demand: Flex_Demand) => {
        let start = new Date(demand.start_time);
        let end = new Date(demand.end_time);
        return start.toTimeString().split(' ')[0] + " - " + end.toTimeString().split(' ')[0];
    }

    /**
     * If flexDemand is truthy, then set filteredFlexDemandData to the result of mapping flexDemand to
     * a new array of Filtered_Flex_Data objects, where each object is a copy of the corresponding
     * flexDemand object with a new categoryField property set to the result of calling
     * getTooltipForDemand on the corresponding flexDemand object.
     */
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

    /**
     * It takes a Flex_Offer object, creates two Date objects from the start_time and end_time
     * properties of the Flex_Offer object, and returns a string that is the start time and end time of
     * the Flex_Offer object.
     * @param {Flex_Offer} offer - Flex_Offer
     * @returns A function that takes an offer and returns a string.
     */
    const getTooltipForOffer = (offer: Flex_Offer) => {
        let start = new Date(offer.start_time);
        let end = new Date(offer.end_time);
        return start.toTimeString().split(' ')[0] + " - " + end.toTimeString().split(' ')[0];
    }

    /**
     * If flexOffers is not null, then map over flexOffers and return a new array of Filtered_Flex_Data
     * objects.
     */
    const setFilteredFlexDataFromOffers = () => {
        if (flexOffers) {
            let data: Filtered_Flex_Data[] = flexOffers.map((offer) => {
                offer.offered_flexibility = Math.round(offer.offered_flexibility * 100) / 100;
                let tooltipTxt = getTooltipForOffer(offer);
                return {
                    start_time: offer.start_time,
                    end_time: offer.end_time,
                    flexibility: offer.offered_flexibility,
                    categoryField: tooltipTxt,
                    percentage: Math.round(offer.offered_flexibility/offer.requested_flexibility*100),
                }
            }) as Filtered_Flex_Data[];
            if (data) {
                setFilteredFlexOfferData(data);
            }
        }
    }

    /* Creating a new object and assigning it to the variable algorithmRequest. */
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

    /**
     * GetAlgorithmData() is a function that calls setAlgorithmRequest() and then dispatches the result
     * of setAlgorithmRequest() to the reducer.
     */
    const getAlgorithmData = () => {
        let algorithmRequest = setAlgorithmRequest();
        dispatch(getAlgorithmDataStart(algorithmRequest));
    }

    /**
     * When the user clicks on the button, the user will be navigated to the insight page.
     */
    const toInsightAnalytics = () => {
        navigate("/insight");
    }

    /**
     * When the user clicks on the button, the user will be navigated to the buildings page.
     */
    const toBuildings = () => {
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

    /**
     * If flexDemand is true, then map over flexDemand and return the result of
     * getTooltipForDemand(demand) and set the result to categories.
     */
    const defineCategories = () => {
        if (flexDemand) {
            let ctgs = flexDemand.map((demand) => {
                return getTooltipForDemand(demand);
            })
            if (ctgs) {
                setCategories(ctgs);
            }
        }
    }

    /**
     * If the currentUser is defined, then create a new object called algorithmResponse, and then
     * dispatch the sendFlexOfferStart function with the currentUser.user_id and algorithmResponse as
     * parameters.
     */
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

    /**
     * OnSliderValueChange is a function that takes an event of type SliderChangeEvent and sets
     * sliderPct with value.
     * @param {SliderChangeEvent} event - SliderChangeEvent - The event object that is passed to the
     * event handler.
     */
    const onSliderValueChange = (event: SliderChangeEvent) => {
        setSliderPct(Math.round(event.value * 10) / 10);
    }

    /* A function that returns a ChartSeriesItem. */
    const renderBarChartSeriesItem = (items: Filtered_Flex_Data[], color?: string, showKWH?: boolean) => {
        let mesurement_unit = 'kWh';
        let field_ = 'flexibility';
        if (showKWH===false) {
            mesurement_unit = "%";
            field_ = 'percentage';
        }
        return <ChartSeriesItem
                    key={'demand'}
                    type="column"
                    tooltip={{ visible: true, format: "{0} " + mesurement_unit }}
                    data={items}
                    field={field_}
                    categoryField={'categoryField'}
                    color={color ? color : '#CC00FF'}/>
    }

    /**
     * When the button is clicked, call the getAlgorithmData() function.
     */
    const onButtonReloadClick = () => {
        getAlgorithmData();
    }
    
    return (
        <>
            <RowContainer>
                <SpinnerContainer>
                    {(algorithmIsLoading || flexDemandIsLoading) && <Loader size="large"  type="converging-spinner" />}
                </SpinnerContainer>
                <DatePickerContainer>
                    <DatePicker defaultValue={tomorrow} format={"dd.MM.yyyy"} onChange={onChangeSelectedDate} />
                </DatePickerContainer>
                <GraphContainer>
                    {
                        filteredFlexDemandData &&
                        <Chart style={{ height: 250, width: '99%' }}> 
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
                    <RowContainer>
                        {
                            filteredFlexOfferData.length>0 &&
                            (
                                showKWH ?
                                <Button
                                    onClick={() => {setShowKWH(false)}}
                                    themeColor="info"
                                    disabled={(currentUser === null) || algorithmIsLoading || flexDemandIsLoading}
                                    style={{ margin: '5px', width: 200, alignSelf: 'center'}}>
                                    Show %
                                </Button>
                                :
                                <Button
                                    onClick={() => {setShowKWH(true)}}
                                    themeColor="info"
                                    disabled={(currentUser === null) || algorithmIsLoading || flexDemandIsLoading}
                                    style={{ margin: '5px', width: 200, alignSelf:'center' }}>
                                    Show kWh
                                </Button>
                            )
                        }
                    </RowContainer>
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
                                        renderBarChartSeriesItem(filteredFlexOfferData, "green", showKWH)
                                    }
                            </ChartSeries>
                        </Chart>
                    }
                    <CustomContainer>
                        <SliderContainer>
                            <Label editorId="slider1">{sliderPct + "%"}</Label>
                            <Slider id="slider1" min={0} max={100} step={1} defaultValue={sliderPct} onChange={onSliderValueChange} />
                            <Button
                                onClick={onButtonReloadClick}
                                themeColor="tertiary"
                                disabled={(currentUser === null) ||  algorithmIsLoading || flexDemandIsLoading}
                                style={{ margin: '5px' }}>
                                Load VPP configuration</Button>
                        </SliderContainer>
                        
                    </CustomContainer>
                </GraphContainer>
                
            </RowContainer>

            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "center" } as FloatingActionButtonAlign}
                text={'Insights & Analytics'}
                disabled={(currentUser === null) || (flexOffers === undefined) || (algorithmIsLoading === true) || (flexDemandIsLoading === true)}
                onClick={toInsightAnalytics} />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "start" } as FloatingActionButtonAlign}
                text={'Go back to the building portfolio'}
                onClick={toBuildings}
                themeColor="inverse" />
            <FloatingActionButton
                align={{ vertical: "bottom", horizontal: "end" } as FloatingActionButtonAlign}
                text={'Submit'}
                disabled={(currentUser===null) || (flexOffers===undefined) || (algorithmIsLoading===true) || (flexDemandIsLoading===true)}
                onClick={onSubmit}
                themeColor="tertiary" />

            {

                <NotificationGroup
                    style={{
                        right: 170,
                        bottom: 0,
                        alignItems: "flex-start",
                        flexWrap: "wrap-reverse",
                    }}
                >
                    <Fade>
                        {success && (
                            <Notification
                                type={{ style: "success", icon: true }}
                                closable={true}
                                onClose={() => { setSuccess(false) }}
                            >
                                <span>Your data has been saved.</span>
                            </Notification>
                        )}
                    </Fade>
                    <Fade>
                        {error && (
                            <Notification
                                type={{ style: "error", icon: true }}
                                closable={true}
                                onClose={() => { setError(false) }}
                            >
                                <span>Oops! Something went wrong ...</span>
                            </Notification>
                        )}
                    </Fade>

                </NotificationGroup>
            }
            <Outlet />
        </>
    );

};

export default FlexRequests;