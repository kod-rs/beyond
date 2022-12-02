import { takeLatest, put, all, call } from 'redux-saga/effects';
import { FLEX_DEMAND_ACTION_TYPES } from './flex.types';

import {
    getFlexDemandSuccess,
    getFlexDemandFailed,  
    setFlexIsLoading,
} from './flex.action';

import {
    getFlexDemandData,
} from '../../utils/api/api.utils';

export function* getFlexDemand({ payload: { date } }) {
    try {
        yield put(setFlexIsLoading(true));
        let flexDemandResponse = yield call(
            getFlexDemandData,
            date
        );
        if (flexDemandResponse) {
            yield put(getFlexDemandSuccess(flexDemandResponse.demands));
        } else {
            yield put(getFlexDemandFailed("Flex demand was null!"));
        }
    } catch (error) {
        yield put(getFlexDemandFailed(error));
    }
}

export function* onGetFlexDemandStart() {
    yield takeLatest(FLEX_DEMAND_ACTION_TYPES.GET_FLEX_DEMAND_START, getFlexDemand);
}

export function* flexDemandSagas() {
    yield all([
        call(onGetFlexDemandStart),
    ]);
}
