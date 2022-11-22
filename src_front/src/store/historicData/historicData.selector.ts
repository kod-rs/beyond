import { createSelector } from 'reselect';

import { BuildingsState } from './historicData.reducer';
import { RootState } from '../store';

export const selectBuildingsReducer = (state: RootState): BuildingsState => state.buildings;

export const selectBuildingsForCurrentUser = createSelector(
    selectBuildingsReducer,
    (buildingsState) => buildingsState.buildings
);
