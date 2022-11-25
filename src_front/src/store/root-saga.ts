import { all, call } from 'redux-saga/effects';
import { userSagas } from './user/user.saga';
import { buildingsSagas } from './buildings/buildings.saga';
import { historicDataSagas } from './historicData/historicData.saga';
import { flexDemandSagas } from './flexDemand/flex.saga';
import { algorithmDataSagas } from './algorithm/algorithm.saga';


export function* rootSaga() {
    yield all([
        call(buildingsSagas),
        call(userSagas),
        call(historicDataSagas),
        call(flexDemandSagas),
        call(algorithmDataSagas)
    ]);
}
