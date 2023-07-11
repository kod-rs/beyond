/* Defining the action types for the reducer. */
export enum BUILDINGS_ACTION_TYPES {
    GET_BUILDINGS_START = 'buildings/GET_BUILDINGS_START',
    GET_BUILDINGS_SUCCESS = 'buildings/GET_BUILDINGS_SUCCESS',
    GET_BUILDINGS_FAILED = 'buildings/GET_BUILDINGS_FAILED',
    SET_BUILDINGS = 'buildings/SET_BUILDINGS',
    SET_IS_LOADING = 'buildings/SET_IS_LOADING',
}

/**
 * A Building is an object with a selected property that is a boolean, a building_id property that is a
 * string, a building_name property that is a string, a latitude property that is a number, and a
 * longitude property that is a number.
 * @property {boolean} selected - boolean;
 * @property {string} building_id - string;
 * @property {string} building_name - string;
 * @property {number} latitude - number;
 * @property {number} longitude - number;
 * @property {string} color - string;
 */
export type Building = {
    selected: boolean;
    building_id: string;
    building_name: string;
    latitude: number;
    longitude: number;
    color: string;
};



