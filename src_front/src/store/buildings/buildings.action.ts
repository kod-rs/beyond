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
export type SetIsLoadingBuildings = ActionWithPayload<BUILDINGS_ACTION_TYPES.SET_IS_LOADING,boolean>;

/* Creating a function that takes a UserData and returns a GetBuildingsStart action. */
export const getBuildingsStart = withMatcher(
    (user: UserData): GetBuildingsStart =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, { user })
);

/* Creating a function that takes a Building[] and returns a GetBuildingsSuccess action. */
export const getBuildingsSuccess = withMatcher(
    (buildings: Building[]): GetBuildingsSuccess =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_SUCCESS, buildings)
);

/* Creating a function that takes an Error and returns a GetBuildingsFailed action. */
export const getBuildingsFailed = withMatcher(
    (error: Error): GetBuildingsFailed =>
        createAction(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_FAILED, error)
);

/* Creating a function that takes a Building[] and returns a SetBuildings action. */
export const setBuildings = withMatcher(
    (buildings: Building[]): SetBuildings =>
        createAction(BUILDINGS_ACTION_TYPES.SET_BUILDINGS, buildings)
);

/* Creating a function that takes a boolean value and returns a SetIsLoadingBuildings action. */
export const setIsLoadingBuildings = withMatcher(
    (value:boolean): SetIsLoadingBuildings =>
        createAction(BUILDINGS_ACTION_TYPES.SET_IS_LOADING, value)
);


