import { createSelector } from 'reselect';
import { AlgorithmDataState } from './algorithm.reducer';
import { RootState } from '../store';

/**
 * It takes the state of the entire application and returns the state of the algorithm data
 * @param {RootState} state - RootState - this is the root state of the application.
 */
export const selectAlgorithmReducer = (state: RootState): AlgorithmDataState => state.algorithmData;

/* Creating a selector for the offers property of the algorithmDataState. */
export const selectAlgorithmData = createSelector(
    selectAlgorithmReducer,
    (algorithmDataState) => algorithmDataState.algorithmData?.offers
);

/* Creating a selector for the isLoading property of the algorithmDataState. */
export const selectAlgorithmDataLoading = createSelector(
    selectAlgorithmReducer,
    (algorithmDataState) => algorithmDataState.isLoading
);

/* Creating a selector for the offer_confirmation_response property of the algorithmDataState. */
export const selectFlexOfferResponse = createSelector(
    selectAlgorithmReducer,
    (algorithmDataState) => algorithmDataState.offer_confirmation_response
);
