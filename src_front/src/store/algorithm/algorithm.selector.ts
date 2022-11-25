import { createSelector } from 'reselect';
import { AlgorithmDataState } from './algorithm.reducer';
import { RootState } from '../store';

export const selectAlgorithmReducer = (state: RootState): AlgorithmDataState => state.algorithmData;

export const selectAlgorithm = createSelector(
    selectAlgorithmReducer,
    (algorithmData) => algorithmData
);
