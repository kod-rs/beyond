import { Flex_Demand, FLEX_DEMAND_ACTION_TYPES } from './flex.types';
import {
  createAction,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';

export type GetFlexDemandStart = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_START, { date: Date }>;
export type GetFlexDemandSuccess = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_SUCCESS, Flex_Demand[]>;
export type GetFlexDemandFailed = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_FAILED, Error>;
export type SetFlexDate = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.SET_FLEX_DATE, { date: Date }>;
export type SetFlexIsLoading = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.SET_IS_LOADING, { value: boolean }>;

/* A function that returns a function that returns an object. */
export const getFlexDemandStart = withMatcher(    
    (date: Date): GetFlexDemandStart =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_START, { date })
);

/* A function that returns a function that returns an object. */
export const getFlexDemandSuccess = withMatcher(
    (FlexDemand: Flex_Demand[]): GetFlexDemandSuccess =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_SUCCESS, FlexDemand)
);

/* A function that returns a function that returns an object. */
export const getFlexDemandFailed = withMatcher(
    (error: Error): GetFlexDemandFailed =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_FAILED, error)
);

/* A function that returns a function that returns an object. */
export const setFlexDateStart = withMatcher(
    (date: Date): SetFlexDate =>
        createAction(FLEX_DEMAND_ACTION_TYPES.SET_FLEX_DATE, { date })
);

/* A function that returns a function that returns an object. */
export const setFlexIsLoading = withMatcher(
    (value: boolean): SetFlexIsLoading =>
        createAction(FLEX_DEMAND_ACTION_TYPES.SET_IS_LOADING, { value })
);
