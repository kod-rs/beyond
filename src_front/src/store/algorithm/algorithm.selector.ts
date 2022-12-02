import { createSelector } from 'reselect';
import { AlgorithmDataState } from './algorithm.reducer';
import { RootState } from '../store';

export const selectAlgorithmReducer = (state: RootState): AlgorithmDataState => state.algorithmData;

export const selectAlgorithmData = createSelector(
    selectAlgorithmReducer,
    (algorithmDataState) => algorithmDataState.algorithmData?.offers
);

export const selectAlgorithmDataLoading = createSelector(
    selectAlgorithmReducer,
    (algorithmDataState) => algorithmDataState.isLoading
);
