/* Defining an enum. */
export enum HISTORIC_DATA_ACTION_TYPES {
    GET_HISTORIC_DATA_START = 'historicData/GET_HISTORIC_DATA_START',
    GET_HISTORIC_DATA_SUCCESS = 'historicData/GET_HISTORIC_DATA_SUCCESS',
    GET_HISTORIC_DATAS_FAILED = 'historicData/GET_HISTORIC_DATAS_FAILED',
    SET_IS_LOADING = 'historicData/SET_IS_LOADING',

 }

/**
 * TimeseriesData is an object with a value property that is a number and a timestamp property that is
 * any type.
 * @property {number} value - The value of the data point.
 * @property {any} timestamp - The timestamp of the data point.
 */
export type TimeseriesData = {
    value: number,
    timestamp: any,
};

/**
 * Building_Info is an object with a building_id property that is a string, and an energy_info property
 * that is an array of TimeseriesData objects.
 * @property {string} building_id - string
 * @property {TimeseriesData[]} energy_info - TimeseriesData[]
 */
export type Building_Info = {
    building_id: string,
    energy_info: TimeseriesData[],
}

/**
 * BUILDING_INFO_Response is a type that has a property called type that is a string, and a property
 * called buildings_info that is an array of Building_Info objects.
 * @property {string} type - string
 * @property {Building_Info[]} buildings_info - Building_Info[]
 */
export type BUILDING_INFO_Response = {
    type: string,
    buildings_info: Building_Info[],
};

