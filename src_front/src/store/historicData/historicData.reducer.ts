import { AnyAction } from 'redux';
import { Building_Info } from './historicData.types';

import {  
    getHistoricDataSuccess,
    getHistoricDataFailed,  
    setIsLoadingHistory,
} from './historicData.action';

/**
 * HistoricDataState is an object with three properties: buildings_info, isLoading, and error. 
 * The buildings_info property is an array of Building_Info objects or null. 
 * The isLoading property is a boolean. 
 * The error property is an Error object or null.
 * @property {Building_Info[] | null} buildings_info - Building_Info[] | null;
 * @property {boolean} isLoading - boolean;
 * @property {Error | null} error - Error | null;
 */
export type HistoricDataState = {
    readonly buildings_info: Building_Info[] | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

/* Setting the initial state of the reducer. */
const INITIAL_STATE: HistoricDataState = {
    buildings_info: null,
    isLoading: false,
    error: null,
};

/**
 * If the action matches the type of the action creator, then return a new state object with the
 * payload of the action.
 * @param state - the current state of the reducer
 * @param action - {type: "GET_HISTORIC_DATA_SUCCESS", payload: Array(1)}
 * @returns The state is being returned.
 */
export const historicDataReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getHistoricDataSuccess.match(action)) {
        return { ...state, buildings_info: action.payload };
    }

    if (getHistoricDataFailed.match(action)) {
        return { ...state, error: action.payload };
    }

    if (setIsLoadingHistory.match(action)) {
        return { ...state, isLoading: action.payload };
    }

    return state;
};
