import { takeLatest, put, all, call } from 'redux-saga/effects';
import { HISTORIC_DATA_ACTION_TYPES } from './historicData.types';

import {
    getHistoricDataSuccess,
    getHistoricDataFailed
} from './historicData.action';

import {
    getBuildingHistoryData,
} from '../../utils/api/api.utils';

export function* getBuildingsHistory({ payload: { buildings } }) {
    try {
        let buildings_info_response = yield call(
            getBuildingHistoryData,
            buildings
        );
        if (buildings_info_response) {
            yield put(getHistoricDataSuccess(buildings_info_response.buildings_info));
        } else {
            yield put(getHistoricDataFailed("Buildings_info were null!"));
        }
    } catch (error) {
        yield put(getHistoricDataFailed(error));
    }
}

export function* onGetBuildingsHistoryStart() {
    yield takeLatest(HISTORIC_DATA_ACTION_TYPES.GET_HISTORIC_DATA_START, getBuildingsHistory);
}

export function* historicDataSagas() {
    yield all([
        call(onGetBuildingsHistoryStart),
    ]);
}
