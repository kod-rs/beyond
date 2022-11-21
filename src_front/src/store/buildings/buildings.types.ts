export enum BUILDINGS_ACTION_TYPES {
    GET_BUILDINGS_START = 'buildings/GET_BUILDINGS_START',
    GET_BUILDINGS_SUCCESS = 'buildings/GET_BUILDINGS_SUCCESS',
    GET_BUILDINGS_FAILED = 'buildings/GET_BUILDINGS_FAILED',
}

export type Building = {
    selected: boolean;
    building_id: string;
    building_name: string;
    latitude: number;
    longitude: number;
};



