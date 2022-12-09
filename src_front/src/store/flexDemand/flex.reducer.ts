import { AnyAction } from 'redux';
import { Flex_Demand } from './flex.types';

import {  
    getFlexDemandFailed,
    getFlexDemandSuccess,
    setFlexDateStart,
    setFlexIsLoading
} from './flex.action';

/**
 * FlexDemandState is an object with properties flexDemand, flexDate, isLoading, and error, where
 * flexDemand is an array of Flex_Demand objects or null, flexDate is a Date object or null, isLoading
 * is a boolean, and error is an Error object or null.
 * @property {Flex_Demand[] | null} flexDemand - Flex_Demand[] | null;
 * @property {Date | null} flexDate - Date | null;
 * @property {boolean} isLoading - boolean;
 * @property {Error | null} error - Error | null;
 */
export type FlexDemandState = {
    readonly flexDemand: Flex_Demand[] | null;
    readonly flexDate: Date | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

/* Setting the initial state of the reducer. */
const INITIAL_STATE: FlexDemandState = {
    flexDemand: null,
    flexDate: null,
    isLoading: false,
    error: null,
};

/**
 * If the action matches the action type, then return the new state with the payload, otherwise return
 * the current state.
 * @param state - the current state of the reducer
 * @param action - {type: "GET_FLEX_DEMAND_SUCCESS", payload: Array(1)}
 * @returns The state is being returned.
 */
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
