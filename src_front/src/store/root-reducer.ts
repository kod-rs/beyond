import { combineReducers } from 'redux';

import { userReducer } from './user/user.reducer';
import { buildingsReducer } from './buildings/buildings.reducer';
import { historicDataReducer } from './historicData/historicData.reducer';
import { flexDemandReducer } from './flexDemand/flex.reducer';
import { algorithmDataReducer } from './algorithm/algorithm.reducer';


/* Combining all the reducers into one reducer. */
export const rootReducer = combineReducers({
    user: userReducer,
    buildings: buildingsReducer,
    historicData: historicDataReducer,
    flexDemand: flexDemandReducer,
    algorithmData: algorithmDataReducer,
});
