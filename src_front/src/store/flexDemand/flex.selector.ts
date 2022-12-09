import { createSelector } from 'reselect';

import { FlexDemandState } from './flex.reducer';
import { RootState } from '../store';

/**
 * It takes the root state and returns the flex demand state
 * @param {RootState} state - RootState - this is the root state of the application.
 */
export const selectFlexDemandReducer = (state: RootState): FlexDemandState => state.flexDemand;

/* Creating a selector that will return the value of `flexDemand` from the `flexDemandState` object. */
export const selectFlexDemand = createSelector(
    selectFlexDemandReducer,
    (flexDemandState) => flexDemandState.flexDemand
);

/* Creating a selector that will return the value of `flexDate` from the `flexDemandState` object. */
export const selectFlexDate = createSelector(
    selectFlexDemandReducer,
    (flexDemandState) => flexDemandState.flexDate
);

/* Creating a selector that will return the value of `isLoading` from the `flexDemandState` object. */
export const selectFlexIsLoading = createSelector(
    selectFlexDemandReducer,
    (flexDemandState) => flexDemandState.isLoading
);
