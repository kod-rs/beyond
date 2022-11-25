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
    interval: IntervalObj,
    flexibility: number,
}

export type Algorithm_Request = {
    building_energy_list: Building_Info[],
    from: Date,
    to: Date,
    amount: number
}

export type Algorithm_Response = {
    type: string,
    status: boolean,
    offered_flexibility: number,
    interval: IntervalObj,
    building_info: Building_Energy_Info[]
};