import { takeLatest, put, all, call } from 'redux-saga/effects';
import { HISTORIC_DATA_ACTION_TYPES } from './historicData.types';

import {
    getHistoricDataSuccess,
    getHistoricDataFailed,
    setIsLoadingHistory,
} from './historicData.action';

import {
    getBuildingHistoryData,
} from '../../utils/api/api.utils';

/* A generator function that is used to run all the sagas at once. */
export function* getBuildingsHistory({ payload: { buildings } }) {
    try {
        yield put(setIsLoadingHistory(true));
        let buildings_info_response = yield call(
            getBuildingHistoryData,
            buildings
        );
        if (buildings_info_response) {
            yield put(getHistoricDataSuccess(buildings_info_response.buildings_info));
        } else {
            yield put(getHistoricDataFailed("Buildings_info were null!"));
        }
        yield put(setIsLoadingHistory(false));
    } catch (error) {
        yield put(getHistoricDataFailed(error));
        yield put(setIsLoadingHistory(false));
    }
}

/* A generator function that is used to run all the sagas at once. */
export function* onGetBuildingsHistoryStart() {
    yield takeLatest(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, getBuildingsHistory);
}

/* A generator function that is used to run all the sagas at once. */
export function* historicDataSagas() {
    yield all([
        call(onGetBuildingsHistoryStart),
    ]);
}
