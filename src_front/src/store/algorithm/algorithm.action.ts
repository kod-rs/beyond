import { Algorithm_Response, ALGORITHM_ACTION_TYPES, Algorithm_Request } from './algorithm.types';
import {
  createAction,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';

export type GetAlgorithmDataStart = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START, { request: Algorithm_Request }>;
export type GetAlgorithmDataSuccess = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_SUCCESS, Algorithm_Response>;
export type GetAlgorithmDataFailed = ActionWithPayload<ALGORITHM_ACTION_TYPES.GET_ALGORITHM_FAILED, Error>;

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
