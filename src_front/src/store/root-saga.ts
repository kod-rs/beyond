import { all, call } from 'redux-saga/effects';
import { userSagas } from './user/user.saga';
import { buildingsSagas } from './buildings/buildings.saga'

export function* rootSaga() {
    yield all([call(buildingsSagas), call(userSagas)]);
}
