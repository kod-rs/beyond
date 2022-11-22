export enum HISTORIC_DATA_ACTION_TYPES {
    GET_HISTORIC_DATA_START = 'historicData/GET_HISTORIC_DATA_START',
    GET_HISTORIC_DATA_SUCCESS = 'historicData/GET_HISTORIC_DATA_SUCCESS',
    GET_HISTORIC_DATAS_FAILED = 'historicData/GET_HISTORIC_DATAS_FAILED',
    
}

export type Building = {
    selected: boolean;
    building_id: string;
    building_name: string;
    latitude: number;
    longitude: number;
};



