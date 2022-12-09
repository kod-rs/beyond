import { USER_ACTION_TYPES } from './user.types';
import {
  createAction,
  Action,
  ActionWithPayload,
  withMatcher,
} from '../../utils/reducer/reducer.utils';

import {
    UserData,    
} from './user.types';

export type CheckUserSession = Action<USER_ACTION_TYPES.CHECK_USER_SESSION>;
export type EmailSignInStart = ActionWithPayload<USER_ACTION_TYPES.EMAIL_SIGN_IN_START,{ email: string; password: string }>;
export type SignInSuccess = ActionWithPayload<USER_ACTION_TYPES.SIGN_IN_SUCCESS,UserData>;
export type SignInFailed = ActionWithPayload<USER_ACTION_TYPES.SIGN_IN_FAILED,Error>;
export type SignOutStart = Action<USER_ACTION_TYPES.SIGN_OUT_START>;
export type SignOutSuccess = Action<USER_ACTION_TYPES.SIGN_OUT_SUCCESS>;
export type SignOutFailed = ActionWithPayload<USER_ACTION_TYPES.SIGN_OUT_FAILED, Error>;


/* Creating a function that returns an action object. */
export const checkUserSession = withMatcher(
    (): CheckUserSession => createAction(USER_ACTION_TYPES.CHECK_USER_SESSION)
);

/* Creating a function that returns an action object. */
export const emailSignInStart = withMatcher(
    (email: string, password: string): EmailSignInStart =>
        createAction(USER_ACTION_TYPES.EMAIL_SIGN_IN_START, { email, password })
);

/* Creating a function that returns an action object. */
export const signInSuccess = withMatcher(
    (user: UserData): SignInSuccess =>
        createAction(USER_ACTION_TYPES.SIGN_IN_SUCCESS, user)
);

/* Creating a function that returns an action object. */
export const signInFailed = withMatcher(
    (error: Error): SignInFailed =>
        createAction(USER_ACTION_TYPES.SIGN_IN_FAILED, error)
);

/* Creating a function that returns an action object. */
export const signOutStart = withMatcher(
    (): SignOutStart => createAction(USER_ACTION_TYPES.SIGN_OUT_START)
);

/* Creating a function that returns an action object. */
export const signOutSuccess = withMatcher(
    (): SignOutSuccess => createAction(USER_ACTION_TYPES.SIGN_OUT_SUCCESS)
);

/* Creating a function that returns an action object. */
export const signOutFailed = withMatcher(
    (error: Error): SignOutFailed =>
        createAction(USER_ACTION_TYPES.SIGN_OUT_FAILED, error)
);

