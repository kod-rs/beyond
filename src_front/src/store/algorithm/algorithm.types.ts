import { Flex_Demand } from "../flexDemand/flex.types";
import { Building_Info } from "../historicData/historicData.types";

export enum ALGORITHM_ACTION_TYPES {
    GET_ALGORITHM_START = 'flex/GET_ALGORITHM_START',
    GET_ALGORITHM_SUCCESS = 'flex/GET_ALGORITHM_SUCCESS',
    GET_ALGORITHM_FAILED = 'flex/GET_ALGORITHM_FAILED',
}

export type IntervalObj = {
    from: string,
    to: string,
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
