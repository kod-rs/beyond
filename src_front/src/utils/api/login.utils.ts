import { signInWithEmailAndPassword } from './api.utils';
import { UserData } from '../../store/user/user.types';


export type ObjectToAdd = {
  title: string;
};

export const signInAuthUserWithEmailAndPassword = async (email: string, password: string) => {
  if (!email || !password) return;

  return await signInWithEmailAndPassword(email, password);
};

export const signOutUser = async () => await signOut();

const signOut = async () => {
    //TODO add signout logic
    return null
};

//export const getCurrentUser = (): Promise<UserData | null> => {
//  return new Promise((resolve, reject) => {
//      /*TODO get user from global state*/
//      console.log("TODO get user from global state");
//  });
//};
