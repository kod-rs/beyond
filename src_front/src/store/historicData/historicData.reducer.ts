import { AnyAction } from 'redux';
import { Building_Info } from './historicData.types';

import {  
    getHistoricDataSuccess,
    getHistoricDataFailed,  
    setIsLoadingHistory,
} from './historicData.action';

export type HistoricDataState = {
    readonly buildings_info: Building_Info[] | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: HistoricDataState = {
    buildings_info: null,
    isLoading: false,
    error: null,
};

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
