import { AnyAction } from 'redux';
import { Building } from './buildings.types';

import {  
    getBuildingsSuccess,
    getBuildingsFailed,  
    setBuildings
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
        return { ...state, buildings: action.payload };
    }

    if (getBuildingsFailed.match(action)) {
        return { ...state, error: action.payload };
    }

    if (setBuildings.match(action)) {
        return { ...state, buildings: action.payload };
    }
  return state;
};
