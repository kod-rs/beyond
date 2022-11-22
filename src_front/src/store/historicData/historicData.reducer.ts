import { AnyAction } from 'redux';
import { Building } from './historicData.types';

import {  
    getBuildingsSuccess,
    getBuildingsFailed,  
} from './historicData.action';

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

  return state;
};
