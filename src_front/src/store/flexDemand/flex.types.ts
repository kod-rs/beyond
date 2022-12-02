export enum FLEX_DEMAND_ACTION_TYPES {
    GET_FLEX_DEMAND_START = 'flex/GET_FLEX_DEMAND_START',
    GET_FLEX_DEMAND_SUCCESS = 'flex/GET_FLEX_DEMAND_SUCCESS',
    GET_FLEX_DEMAND_FAILED = 'flex/GET_FLEX_DEMAND_FAILED',
    SET_FLEX_DATE = 'flex/SET_FLEX_DATE',
    SET_IS_LOADING = 'flex/SET_IS_LOADING',
}

export type Flex_Demand = {
    start_time: string,
    end_time: string,
    flexibility:number,
}

export type Flex_Demand_Response = {
    type: string,
    demands: Flex_Demand[],
};