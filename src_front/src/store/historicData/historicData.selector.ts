import { createSelector } from 'reselect';

import { HistoricDataState } from './historicData.reducer';
import { RootState } from '../store';

/**
 * It takes the root state and returns the historic data state
 * @param {RootState} state - RootState - this is the root state of the application.
 */
export const selectBuildingsHistoricReducer = (state: RootState): HistoricDataState => state.historicData;

/* Creating a selector that will return the value of `buildings_info` from the `historicData` state. */
export const selectBuildingsHistoricData = createSelector(
    selectBuildingsHistoricReducer,
    (historicData) => historicData.buildings_info
);

/* Creating a selector that will return the value of `isLoading` from the `historicData` state. */
export const selectIsLoadingHistoricData = createSelector(
    selectBuildingsHistoricReducer,
    (historicData) => historicData.isLoading
);
