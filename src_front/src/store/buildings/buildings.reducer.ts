import { AnyAction } from 'redux';
import { Building } from './buildings.types';

import {  
    getBuildingsSuccess,
    getBuildingsFailed,  
    setBuildings,
    setIsLoadingBuildings,
} from './buildings.action';

/**
 * BuildingsState is an object with three properties: buildings, isLoading, and error.
 * @property {Building[] | null} buildings - Building[] | null;
 * @property {boolean} isLoading - boolean;
 * @property {Error | null} error - Error | null;
 */
export type BuildingsState = {
    readonly buildings: Building[] | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

/* Setting the initial state of the buildingsReducer. */
const INITIAL_STATE: BuildingsState = {
    buildings: null,
    isLoading: false,
    error: null,
};

/**
 * If the action matches the action type, then return a new state object with the payload.
 * @param state - The current state of the reducer.
 * @param action - {type: "GET_BUILDINGS_SUCCESS", payload: Array(2)}
 * @returns The state is being returned.
 */
export const buildingsReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getBuildingsSuccess.match(action)) {
        return { ...state, buildings: action.payload, isLoading: false};
    }

    if (getBuildingsFailed.match(action)) {
        return { ...state, error: action.payload, isLoading: false};
    }

    if (setBuildings.match(action)) {
        return { ...state, buildings: action.payload };
    }

    if (setIsLoadingBuildings.match(action)) {
        return { ...state, isLoading: action.payload };
    }
  return state;
};
