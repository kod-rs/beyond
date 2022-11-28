import { Building, BUILDINGS_ACTION_TYPES } from './buildings.types';
import {
  createAction,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';
import { UserData } from '../user/user.types';


export type GetBuildingsStart = ActionWithPayload<BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, {user:UserData}>;
export type GetBuildingsSuccess = ActionWithPayload<BUILDINGS_ACTION_TYPES.GET_BUILDINGS_SUCCESS, Building[]>;
export type GetBuildingsFailed = ActionWithPayload<BUILDINGS_ACTION_TYPES.GET_BUILDINGS_FAILED, Error>;
export type SetBuildings = ActionWithPayload<BUILDINGS_ACTION_TYPES.SET_BUILDINGS, Building[]>;
//Get Buildings For CurrentUser

export const getBuildingsStart = withMatcher(
    (user: UserData): GetBuildingsStart =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, { user })
);

export const getBuildingsSuccess = withMatcher(
    (buildings: Building[]): GetBuildingsSuccess =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_SUCCESS, buildings)
);

export const getBuildingsFailed = withMatcher(
    (error: Error): GetBuildingsFailed =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_FAILED, error)
);

export const setBuildings = withMatcher(
    (buildings: Building[]): SetBuildings =>
        createAction(BUILDINGS_ACTION_TYPES.SET_BUILDINGS, buildings)
);


