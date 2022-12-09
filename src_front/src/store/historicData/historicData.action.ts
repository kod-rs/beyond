import { Building_Info, HISTORIC_DATA_ACTION_TYPES } from './historicData.types';
import {
    createAction,
    ActionWithPayload,
    withMatcher,
} from '../../utils/reducer/reducer.utils';
import { Building } from '../buildings/buildings.types';


export type GetHistoricDataStart = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, { buildings: Building[] }>;
export type GetHistoricDataSuccess = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_SUCCESS, Building_Info[]>;
export type GetHistoricDataFailed = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATAS_FAILED, Error>;
export type SetIsLoadingHistory = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.SET_IS_LOADING, boolean>;

/* Creating a function that returns an object with a type and a payload. */
export const getHistoricDataStart = withMatcher(
    (buildings: Building[]): GetHistoricDataStart =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, { buildings })
);

/* Creating a function that returns an object with a type and a payload. */
export const getHistoricDataSuccess = withMatcher(
    (buildings_info: Building_Info[]): GetHistoricDataSuccess =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_SUCCESS, buildings_info)
);

/* Creating a function that returns an object with a type and a payload. */
export const getHistoricDataFailed = withMatcher(
    (error: Error): GetHistoricDataFailed =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATAS_FAILED, error)
);

/* Creating a function that returns an object with a type and a payload. */
export const setIsLoadingHistory = withMatcher(
    (value: boolean): SetIsLoadingHistory =>
        createAction(HISTORIC_DATA_ACTION_TYPES.SET_IS_LOADING, value)
);
