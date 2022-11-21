import { createSelector } from 'reselect';

import { BuildingsState } from './buildings.reducer';
import { RootState } from '../store';

export const selectBuildingsReducer = (state: RootState): BuildingsState => state.buildings;

export const selectBuildingsForCurrentUser = createSelector(
    selectBuildingsReducer,
    (buildingsState) => buildingsState.buildings
);
