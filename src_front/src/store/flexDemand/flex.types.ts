export enum FLEX_DEMAND_ACTION_TYPES {
    GET_FLEX_DEMAND_START = 'flex/GET_FLEX_DEMAND_START',
    GET_FLEX_DEMAND_SUCCESS = 'flex/GET_FLEX_DEMAND_SUCCESS',
    GET_FLEX_DEMAND_FAILED = 'flex/GET_FLEX_DEMAND_FAILED',
    SET_FLEX_DATE = 'flex/SET_FLEX_DATE',
    SET_IS_LOADING = 'flex/SET_IS_LOADING',
}

/**
 * "Flex_Demand is an object with three properties: start_time, end_time, and flexibility. 
 * start_time and end_time are strings, and flexibility is a number."
 * @property {string} start_time - The time at which the demand is required.
 * @property {string} end_time - The time at which the demand ends.
 * @property {number} flexibility - the amount of flexibility the user has in their schedule
 */
export type Flex_Demand = {
    start_time: string,
    end_time: string,
    flexibility:number,
}

/**
 * A Flex_Demand_Response is an object with a type property that is a string and a demands property
 * that is an array of Flex_Demand objects.
 * @property {string} type - string
 * @property {Flex_Demand[]} demands - Flex_Demand[]
 */
export type Flex_Demand_Response = {
    type: string,
    demands: Flex_Demand[],
};