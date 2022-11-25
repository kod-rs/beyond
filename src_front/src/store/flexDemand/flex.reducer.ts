import { AnyAction } from 'redux';
import { Flex_Demand } from './flex.types';

import {  
    getFlexDemandFailed,
    getFlexDemandStart,  
    getFlexDemandSuccess
} from './flex.action';

export type FlexDemandState = {
    readonly flexDemand: Flex_Demand[] | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: FlexDemandState = {
    flexDemand: null,
    isLoading: false,
    error: null,
};

export const flexDemandReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getFlexDemandSuccess.match(action)) {
        return { ...state, flexDemand: action.payload };
    }

    if (getFlexDemandFailed.match(action)) {
        return { ...state, error: action.payload };
    }

  return state;
};
