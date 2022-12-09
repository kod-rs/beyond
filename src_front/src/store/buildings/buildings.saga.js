import { takeLatest, put, all, call } from 'redux-saga/effects';
import { BUILDINGS_ACTION_TYPES } from './buildings.types';

import {
    getBuildingsSuccess,
    getBuildingsFailed, 
    setIsLoadingBuildings,
} from './buildings.action';

import {
    getBuildingsForUser,
} from '../../utils/api/api.utils';

/* A generator function that is called by the saga middleware. It is a generator function that is
called by the saga middleware. */
export function* getBuildingsForCurrentUser({ payload: { user } }) {
    try {
        yield put(setIsLoadingBuildings(true));
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


/* A generator function that is called by the saga middleware. It is a generator function that is
called by the saga middleware.*/
export function* onGetBuildingsStart() {
    yield takeLatest(BUILDINGS_ACTION_TYPES.GET_BUILDINGS_START, getBuildingsForCurrentUser);
}

/* This is the root saga. It is the saga that is exported to the store. It is the saga that is run by
the saga middleware. */
export function* buildingsSagas() {
    yield all([
        call(onGetBuildingsStart),
    ]);
}
