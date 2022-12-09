import { AnyAction } from 'redux';

import {
    signInSuccess,
    signOutSuccess,
    signInFailed,
    signOutFailed,
} from './user.action';

import { UserData } from './user.types';

/**
 * UserState is an object with three properties: currentUser, isLoading, and error. currentUser is
 * either a UserData object or null, isLoading is a boolean, and error is either an Error object or
 * null.
 * @property {UserData | null} currentUser - The current user data.
 * @property {boolean} isLoading - boolean;
 * @property {Error | null} error - Error | null;
 */
export type UserState = {
    readonly currentUser: UserData | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

/* Setting the initial state of the reducer. */
const INITIAL_STATE: UserState = {
    currentUser: null,
    isLoading: false,
    error: null,
};

/**
 * If the action matches the pattern of a sign in success, then return a new state with the current
 * user set to the payload of the action
 * @param state - The current state of the reducer.
 * @param action - The action that was dispatched.
 * @returns The reducer is returning the state.
 */
export const userReducer = (state = INITIAL_STATE, action = {} as AnyAction) => {
    if (signInSuccess.match(action)) {
        return { ...state, currentUser: action.payload };
    }

    if (signOutSuccess.match(action)) {
        return { ...state, currentUser: null };
    }

    if (signOutFailed.match(action) || signInFailed.match(action)) {
        return { ...state, error: action.payload };
    }

    return state;
};
