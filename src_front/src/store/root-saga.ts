import { all, call } from 'redux-saga/effects';
import { userSagas } from './user/user.saga';
import { buildingsSagas } from './buildings/buildings.saga';
import { historicDataSagas } from './historicData/historicData.saga';


export function* rootSaga() {
    yield all([call(buildingsSagas), call(userSagas), call(historicDataSagas)]);
}
