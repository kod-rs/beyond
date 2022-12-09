import { takeLatest, put, all, call } from 'redux-saga/effects';
import { ALGORITHM_ACTION_TYPES } from './algorithm.types';

import {
    setAlgorithmDataLoading,
    getAlgorithmDataSuccess,
    getAlgorithmDataFailed,
    sendFlexOfferSuccess,
    sendFlexOfferFailed
} from './algorithm.action';

import {
    getAlgorithmData,
    sendFlexOffer,
} from '../../utils/api/api.utils';

/* A generator function that is listening for the action type
`ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START` and when it is dispatched, it will call the function
`getAlgorithm` */
export function* getAlgorithm({ payload: { request } }) {
    try {
        yield put(setAlgorithmDataLoading(true));
        let algorithmDataResponse = yield call(
            getAlgorithmData,
            request
        );
        if (algorithmDataResponse) {
            if (algorithmDataResponse.status) {
                yield put(getAlgorithmDataSuccess(algorithmDataResponse));
            } else {
                yield put(getAlgorithmDataFailed(algorithmDataResponse.message));
            }
        } else {
            yield put(getAlgorithmDataFailed("Algorithm data was null!"));
        }
    } catch (error) {
        yield put(getAlgorithmDataFailed(error));
    }
}

/* A generator function that is listening for the action type
`ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_START` and when it is dispatched, it will call the function
`sendOffer` */
export function* sendOffer({ payload: { user_id, response } }) {
    try {
        yield put(setAlgorithmDataLoading(true));
        let sendOfferResponse = yield call(
            sendFlexOffer,
            user_id,
            response
        );
        if (sendOfferResponse) {
            yield put(sendFlexOfferSuccess(sendOfferResponse));
        } else {
            yield put(sendFlexOfferFailed("SendOfferResponse data was null!"));
        }
    } catch (error) {
        yield put(sendFlexOfferFailed(error));
    }
}

/* Listening for the action type `ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START` and when it is
dispatched, it will call the function `getAlgorithm` */
export function* onGetAlgorithmDataStart() {
    yield takeLatest(ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START, getAlgorithm);
}

/* Listening for the action type `ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_START` and when it is
dispatched, it will call the function `sendOffer` */
export function* onSendFlexOfferStart() {
    yield takeLatest(ALGORITHM_ACTION_TYPES.SEND_FLEX_OFFER_START, sendOffer);
}

/* A generator function that is used to run all the sagas at once. */
export function* algorithmDataSagas() {
    yield all([
        call(onGetAlgorithmDataStart),
        call(onSendFlexOfferStart),
    ]);
}
