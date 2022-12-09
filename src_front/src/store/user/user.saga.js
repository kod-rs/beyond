import { takeLatest, put, all, call } from 'redux-saga/effects';
import { USER_ACTION_TYPES } from './user.types';

import {
  signInSuccess,
  signInFailed,
  signOutSuccess,
  signOutFailed,
} from './user.action';

import {  
  signInAuthUserWithEmailAndPassword,
  signOutUser,
} from '../../utils/api/login.utils';

/* A generator function that is being called by the signInWithEmailSaga. */
export function* signInWithEmail({ payload: { email, password } }) {
    try {
        let user = yield call(
            signInAuthUserWithEmailAndPassword,
            email,
            password
        );
        if (user) {
            if (user.status) {
                yield put(signInSuccess(user));
            } else {
                put(signInFailed(user.message));
            }
        } else {
            put(signInFailed("User was null!"));
        }
    } catch (error) {
        yield put(signInFailed(error));
    }
}


/* Calling the signOutUser function and then dispatching the signOutSuccess action. */
export function* signOut() {
  try {
    yield call(signOutUser);
    yield put(signOutSuccess());
  } catch (error) {
    yield put(signOutFailed(error));
  }
}

/* Listening for the EMAIL_SIGN_IN_START action and then calling the signInWithEmail function. */
export function* onEmailSignInStart() {
  yield takeLatest(USER_ACTION_TYPES.EMAIL_SIGN_IN_START, signInWithEmail);
}

/* Listening for the SIGN_OUT_START action and then calling the signOut function. */
export function* onSignOutStart() {
  yield takeLatest(USER_ACTION_TYPES.SIGN_OUT_START, signOut);
}

/* A generator function that is used to run all the sagas at once. */
export function* userSagas() {
    yield all([
        call(onEmailSignInStart),
        call(onSignOutStart),
  ]);
}
