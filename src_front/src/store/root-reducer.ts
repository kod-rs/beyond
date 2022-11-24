import { combineReducers } from 'redux';

import { userReducer } from './user/user.reducer';
import { buildingsReducer } from './buildings/buildings.reducer';
import { historicDataReducer } from './historicData/historicData.reducer';


export const rootReducer = combineReducers({
    user: userReducer,
    buildings: buildingsReducer,
    historicData: historicDataReducer,
});
