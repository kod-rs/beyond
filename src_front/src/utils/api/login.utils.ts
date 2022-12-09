import { signInWithEmailAndPassword } from './api.utils';
import { UserData } from '../../store/user/user.types';


/**
 * ObjectToAdd is an object with a title property that is a string.
 * @property {string} title - string;
 */
export type ObjectToAdd = {
  title: string;
};

/**
 * If the email and password are not empty, then sign in the user with the email and password.
 * @param {string} email - string, password: string
 * @param {string} password - string
 * @returns a promise.
 */
export const signInAuthUserWithEmailAndPassword = async (email: string, password: string) => {
  if (!email || !password) return;

  return await signInWithEmailAndPassword(email, password);
};

/**
 * It calls the signOut function from the Firebase library and returns the result
 */
export const signOutUser = async () => await signOut();

/**
 * This function returns null.
 * @returns null
 */
const signOut = async () => {
    //TODO add signout logic
    return null
};


