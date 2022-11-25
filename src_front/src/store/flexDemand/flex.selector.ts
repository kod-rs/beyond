import { createSelector } from 'reselect';

import { FlexDemandState } from './flex.reducer';
import { RootState } from '../store';

export const selectFlexDemandReducer = (state: RootState): FlexDemandState => state.flexDemand;

export const selectFlexDemand = createSelector(
    selectFlexDemandReducer,
    (flexDemandState) => flexDemandState.flexDemand
);
