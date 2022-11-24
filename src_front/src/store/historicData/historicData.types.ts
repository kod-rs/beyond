export enum HISTORIC_DATA_ACTION_TYPES {
    GET_HISTORIC_DATA_START = 'historicData/GET_HISTORIC_DATA_START',
    GET_HISTORIC_DATA_SUCCESS = 'historicData/GET_HISTORIC_DATA_SUCCESS',
    GET_HISTORIC_DATAS_FAILED = 'historicData/GET_HISTORIC_DATAS_FAILED',
 }

export type TimeseriesData = {
    value: number,
    timestamp: any,
};

export type Building_Info = {
    building_id: string,
    energy_info: TimeseriesData[],
}

export type BUILDING_INFO_Response = {
    type: string,
    buildings_info: Building_Info[],
};

