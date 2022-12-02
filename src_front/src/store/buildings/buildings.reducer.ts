import { AnyAction } from 'redux';
import { Building } from './buildings.types';

import {  
    getBuildingsSuccess,
    getBuildingsFailed,  
    setBuildings,
    setIsLoadingBuildings,
} from './buildings.action';

export type BuildingsState = {
    readonly buildings: Building[] | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: BuildingsState = {
    buildings: null,
    isLoading: false,
    error: null,
};

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
