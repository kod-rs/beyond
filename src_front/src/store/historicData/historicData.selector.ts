import { createSelector } from 'reselect';

import { HistoricDataState } from './historicData.reducer';
import { RootState } from '../store';

export const selectBuildingsHistoricReducer = (state: RootState): HistoricDataState => state.historicData;

export const selectBuildingsHistoricData = createSelector(
    selectBuildingsHistoricReducer,
    (historicData) => historicData.buildings_info
);

export const selectIsLoadingHistoricData = createSelector(
    selectBuildingsHistoricReducer,
    (historicData) => historicData.isLoading
);
