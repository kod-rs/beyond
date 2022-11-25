import { AnyAction } from 'redux';
import { Algorithm_Response } from './algorithm.types';
import {  
    getAlgorithmDataFailed,
    getAlgorithmDataStart,  
    getAlgorithmDataSuccess
} from './algorithm.action';


export type AlgorithmDataState = {
    readonly algorithmData: Algorithm_Response | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: AlgorithmDataState = {
    algorithmData: null,
    isLoading: false,
    error: null,
};

export const algorithmDataReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getAlgorithmDataSuccess.match(action)) {
        return { ...state, algorithmData: action.payload };
    }

    if (getAlgorithmDataFailed.match(action)) {
        return { ...state, error: action.payload };
    }

  return state;
};
