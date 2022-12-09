import { createSelector } from 'reselect';

import { BuildingsState } from './buildings.reducer';
import { RootState } from '../store';

/**
 * It takes the root state and returns the buildings state
 * @param {RootState} state - RootState - this is the root state of the application.
 */
export const selectBuildingsReducer = (state: RootState): BuildingsState => state.buildings;

/* Creating a selector that will return the buildings property from the buildings reducer. */
export const selectBuildingsForCurrentUser = createSelector(
    selectBuildingsReducer,
    (buildingsState) => buildingsState.buildings
);

/* Creating a selector that will return the isLoading property from the buildings reducer. */
export const selectIsLoadingBuildings = createSelector(
    selectBuildingsReducer,
    (buildingsState) => buildingsState.isLoading
);

/* Creating a selector that will return the error from the buildings reducer. */
export const selectGetBuildingsError = createSelector(
    selectBuildingsReducer,
    (buildingsState) => buildingsState.error
);
