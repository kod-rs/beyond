import { takeLatest, put, all, call } from 'redux-saga/effects';
import { ALGORITHM_ACTION_TYPES } from './algorithm.types';

import {
    getAlgorithmDataStart,
    getAlgorithmDataSuccess,
    getAlgorithmDataFailed,  
} from './algorithm.action';

import {
    getAlgorithmData,
} from '../../utils/api/api.utils';

export function* getAlgorithm({ payload: { request } }) {
    try {
        //console.log('getBuildingsForCurrentUser hit!');
        let algorithmDataResponse = yield call(
            getAlgorithmData,
            request
        );
        if (algorithmDataResponse) {
            yield put(getAlgorithmDataSuccess(algorithmDataResponse));
        } else {
            yield put(getAlgorithmDataFailed("Algorithm data was null!"));
        }
    } catch (error) {
        yield put(getAlgorithmDataFailed(error));
    }
}

export function* onGetAlgorithmDataStart() {
    yield takeLatest(ALGORITHM_ACTION_TYPES.GET_ALGORITHM_START, getAlgorithm);
}

export function* algorithmDataSagas() {
    yield all([
        call(onGetAlgorithmDataStart),
    ]);
}
