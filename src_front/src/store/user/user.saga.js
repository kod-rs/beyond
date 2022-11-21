import { takeLatest, put, all, call } from 'redux-saga/effects';
import { USER_ACTION_TYPES } from './user.types';

import {
  signInSuccess,
  signInFailed,
  signOutSuccess,
  signOutFailed,
} from './user.action';

import {
  //getCurrentUser,
  signInAuthUserWithEmailAndPassword,
  signOutUser,
} from '../../utils/api/login.utils';


//export function* returnCurrentUser() {
//    try {
//        let currentUser = yield call(getCurrentUser);
//        currentUser.then((user) => { return user; });
//        //if (currentUser) {
//        //    return currentUser;
//        //}
//    } catch (error) {
//        yield put(signInFailed(error));
//    }
//}


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

export function* signOut() {
  try {
    yield call(signOutUser);
    yield put(signOutSuccess());
  } catch (error) {
    yield put(signOutFailed(error));
  }
}

export function* onEmailSignInStart() {
  yield takeLatest(USER_ACTION_TYPES.EMAIL_SIGN_IN_START, signInWithEmail);
}

export function* onSignOutStart() {
  yield takeLatest(USER_ACTION_TYPES.SIGN_OUT_START, signOut);
}

export function* userSagas() {
    yield all([
        //call(returnCurrentUser),
        call(onEmailSignInStart),
        call(onSignOutStart),
  ]);
}
