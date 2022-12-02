import { Algorithm_Response, ALGORITHM_ACTION_TYPES, Algorithm_Request, Flexibility_Offer_Confirmation_Response } from './algorithm.types';
import {
  createAction,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';

export type GetAlgorithmDataStart = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START, { request: Algorithm_Request }>;
export type GetAlgorithmDataSuccess = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_SUCCESS, Algorithm_Response>;
export type GetAlgorithmDataFailed = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_FAILED, Error>;

export type SendFlexOfferStart = ActionWithPayload<ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_START, { user_id: string, response: Algorithm_Response }>;
export type SendFlexOfferSuccess = ActionWithPayload<ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_SUCCESS, Flexibility_Offer_Confirmation_Response>;
export type SendFlexOfferFailed = ActionWithPayload<ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_FAILED, Error>;

export const getAlgorithmDataStart = withMatcher(
    (request: Algorithm_Request): GetAlgorithmDataStart =>
        createAction(ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START, { request })
);

export const getAlgorithmDataSuccess = withMatcher(
    (AlgorithmData: Algorithm_Response): GetAlgorithmDataSuccess =>
        createAction(ALGORITHM_ACTION_TYPES.GET_ALGORITHM_SUCCESS, AlgorithmData)
);

export const getAlgorithmDataFailed = withMatcher(
    (error: Error): GetAlgorithmDataFailed =>
        createAction(ALGORITHM_ACTION_TYPES.GET_ALGORITHM_FAILED, error)
);

export const sendFlexOfferStart = withMatcher(
    (user_id: string, response: Algorithm_Response): SendFlexOfferStart =>
        createAction(ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_START, { user_id, response })
);

export const sendFlexOfferSuccess = withMatcher(
    (confirmation_Response: Flexibility_Offer_Confirmation_Response): SendFlexOfferSuccess =>
        createAction(ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_SUCCESS, confirmation_Response)
);

export const sendFlexOfferFailed = withMatcher(
    (error: Error): SendFlexOfferFailed =>
        createAction(ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_FAILED, error)
);
