import { Flex_Demand, FLEX_DEMAND_ACTION_TYPES } from './flex.types';
import {
  createAction,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';

export type GetFlexDemandStart = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_START, { date:Date }>;
export type GetFlexDemandSuccess = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_SUCCESS, Flex_Demand[]>;
export type GetFlexDemandFailed = ActionWithPayload<FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_FAILED, Error>;

export const getFlexDemandStart = withMatcher(
    (date: Date): GetFlexDemandStart =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_START, { date })
);

export const getFlexDemandSuccess = withMatcher(
    (FlexDemand: Flex_Demand[]): GetFlexDemandSuccess =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_SUCCESS, FlexDemand)
);

export const getFlexDemandFailed = withMatcher(
    (error: Error): GetFlexDemandFailed =>
        createAction(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_FAILED, error)
);
