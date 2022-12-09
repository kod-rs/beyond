import { createSelector } from 'reselect';
import { UserState } from './user.reducer';
import { RootState } from '../store';

/**
 * This function takes a state object and returns the user property of that state object.
 * @param {RootState} state - RootState - this is the state of the entire application.
 */
export const selectUserReducer = (state: RootState): UserState => state.user;

/* Creating a selector that will return the current user. */
export const selectCurrentUser = createSelector(
  [selectUserReducer],
    (userState) => {
        return userState.currentUser;
    }
);
