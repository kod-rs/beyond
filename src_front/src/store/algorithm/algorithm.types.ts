import { Flex_Demand } from "../flexDemand/flex.types";
import { Building_Info } from "../historicData/historicData.types";

export enum ALGORITHM_ACTION_TYPES {
    GET_ALGORITHM_START = 'flex/GET_ALGORITHM_START',
    GET_ALGORITHM_SUCCESS = 'flex/GET_ALGORITHM_SUCCESS',
    GET_ALGORITHM_FAILED = 'flex/GET_ALGORITHM_FAILED',

    SEND_FLEX_OFFER_START = 'flex/SEND_FLEX_OFFER_START',
    SEND_FLEX_OFFER_SUCCESS = 'flex/SEND_FLEX_OFFER_SUCCESS',
    SEND_FLEX_OFFER_FAILED = 'flex/SEND_FLEX_OFFER_FAILED',

    SET_IS_LOADING = 'flex/SET_IS_LOADING_ALGORITHM',
}

export type Building_Energy_Info = {
    building_id: string,
    start_time: string, //RFC 3339 format
    end_time: string,   //RFC 3339 format
    flexibility: number,
}

export type Algorithm_Request = {
    building_energy_list: Building_Info[],
    flexibility_demands: Flex_Demand[],
}

export type Algorithm_Response = {
    type: string,
    status: boolean,
    offers: Flex_Offer[],
};

export type Flex_Offer = {
    offered_flexibility: number,
    requested_flexibility: number 
    start_time: string, //RFC 3339 format
    end_time: string, //RFC 3339 format
    building_info: Building_Energy_Info[],
}

export type Flexibility_Offer_Confirmation_Response = {
    type: string,
    status: boolean,
}
