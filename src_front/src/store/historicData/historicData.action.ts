import { Building, HISTORIC_DATA_ACTION_TYPES } from './historicData.types';
import {
  createAction,
  Action,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';
import { UserData } from '../user/user.types';


export type GetHistoricDataStart = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, {user:UserData}>;
export type GetHistoricDataSuccess = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_SUCCESS, Building[]>;
export type GetHistoricDataFailed = ActionWithPayload<HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATAS_FAILED, Error>;

//Get Buildings For CurrentUser

export const getBuildingsStart = withMatcher(
    (user: UserData): GetHistoricDataStart =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, { user })
);

export const getBuildingsSuccess = withMatcher(
    (buildings: Building[]): GetHistoricDataSuccess =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_SUCCESS, buildings)
);

export const getBuildingsFailed = withMatcher(
    (error: Error): GetHistoricDataFailed =>
        createAction(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATAS_FAILED, error)
);




