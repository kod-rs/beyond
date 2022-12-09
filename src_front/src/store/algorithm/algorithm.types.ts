import { Flex_Demand } from "../flexDemand/flex.types";
import { Building_Info } from "../historicData/historicData.types";

/* It's defining an enum. */
export enum ALGORITHM_ACTION_TYPES {
    GET_ALGORITHM_START = 'flex/GET_ALGORITHM_START',
    GET_ALGORITHM_SUCCESS = 'flex/GET_ALGORITHM_SUCCESS',
    GET_ALGORITHM_FAILED = 'flex/GET_ALGORITHM_FAILED',
    SEND_FLEX_OFFER_START = 'flex/SEND_FLEX_OFFER_START',
    SEND_FLEX_OFFER_SUCCESS = 'flex/SEND_FLEX_OFFER_SUCCESS',
    SEND_FLEX_OFFER_FAILED = 'flex/SEND_FLEX_OFFER_FAILED',
    SET_IS_LOADING = 'flex/SET_IS_LOADING_ALGORITHM',
}

/**
 * Building_Energy_Info is an object with four properties: building_id, start_time, end_time, and
 * flexibility.
 * @property {string} building_id - The building ID.
 * @property {string} start_time - The start time of the time interval for which the energy information
 * is provided.
 * @property {string} end_time - The end time of the building's energy consumption.
 * @property {number} flexibility - The amount of energy that can be used or produced by the building.
 */
export type Building_Energy_Info = {
    building_id: string,
    start_time: string, //RFC 3339 format
    end_time: string,   //RFC 3339 format
    flexibility: number,
}

/**
 * Algorithm_Request is an object with two properties: building_energy_list and flexibility_demands.
 * building_energy_list is an array of Building_Info objects, and flexibility_demands is an array of
 * Flex_Demand objects.
 * @property {Building_Info[]} building_energy_list - An array of Building_Info objects.
 * @property {Flex_Demand[]} flexibility_demands - Flex_Demand[]
 */
export type Algorithm_Request = {
    building_energy_list: Building_Info[],
    flexibility_demands: Flex_Demand[],
}

/**
 * Algorithm_Response is a type that has a type, a status, and an array of Flex_Offer objects.
 * @property {string} type - string - the type of the response, in this case, it's "algorithm_response"
 * @property {boolean} status - boolean
 * @property {Flex_Offer[]} offers - Flex_Offer[]
 */
export type Algorithm_Response = {
    type: string,
    status: boolean,
    offers: Flex_Offer[],
};

/**
 * A Flex_Offer is a JSON object with four properties: offered_flexibility, requested_flexibility,
 * start_time, and end_time. 
 * The start_time and end_time properties are strings in RFC 3339 format. 
 * The building_info property is an array of Building_Energy_Info objects.
 * @property {number} offered_flexibility - The amount of flexibility that the building is offering to
 * the grid.
 * @property {number} requested_flexibility - The amount of flexibility requested by the building.
 * @property {string} start_time - The start time of the flex offer.
 * @property {string} end_time - The end time of the flex offer.
 * @property {Building_Energy_Info[]} building_info - This is an array of Building_Energy_Info objects.
 */
export type Flex_Offer = {
    offered_flexibility: number,
    requested_flexibility: number 
    start_time: string, //RFC 3339 format
    end_time: string, //RFC 3339 format
    building_info: Building_Energy_Info[],
}

/**
 * Flexibility_Offer_Confirmation_Response is a type that has two properties: type and status. Type is
 * a string and status is a boolean.
 * @property {string} type - string,
 * @property {boolean} status - boolean,
 */
export type Flexibility_Offer_Confirmation_Response = {
    type: string,
    status: boolean,
}
