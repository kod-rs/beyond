import { takeLatest, put, all, call } from 'redux-saga/effects';
import { HISTORIC_DATA_ACTION_TYPES } from './historicData.types';

import {
    getBuildingsStart,
    getBuildingsSuccess,
    getBuildingsFailed,  
} from './historicData.action';

import {
    getBuildingsForUser,
} from '../../utils/api/api.utils';

export function* getBuildingsForCurrentUser({ payload: { user } }) {
    try {
        console.log('getBuildingsForCurrentUser hit!');
        let buildings = yield call(
            getBuildingsForUser,
            user
        );
        if (buildings) {
            yield put(getBuildingsSuccess(buildings.buildings));
        } else {
            yield put(getBuildingsFailed("Buildings for user " + user.displayName + " were null!"));
        }
    } catch (error) {
        yield put(getBuildingsFailed(error));
    }
}

export function* onGetBuildingsStart() {
    yield takeLatest(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, getBuildingsForCurrentUser);
}

export function* buildingsSagas() {
    yield all([
        call(onGetBuildingsStart),
    ]);
}
