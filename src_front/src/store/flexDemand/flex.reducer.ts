import { AnyAction } from 'redux';
import { Flex_Demand } from './flex.types';

import {  
    getFlexDemandFailed,
    getFlexDemandSuccess,
    setFlexDateStart,
    setFlexIsLoading
} from './flex.action';

export type FlexDemandState = {
    readonly flexDemand: Flex_Demand[] | null;
    readonly flexDate: Date | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: FlexDemandState = {
    flexDemand: null,
    flexDate: null,
    isLoading: false,
    error: null,
};

export const flexDemandReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getFlexDemandSuccess.match(action)) {
        return { ...state, flexDemand: action.payload, isLoading: false };
    }

    if (getFlexDemandFailed.match(action)) {
        return { ...state, error: action.payload, isLoading: false };
    }

    if (setFlexDateStart.match(action)) {
        return { ...state, flexDate: action.payload };
    }

    if (setFlexIsLoading.match(action)) {
        return { ...state, isLoading: action.payload };
    }

  return state;
};
