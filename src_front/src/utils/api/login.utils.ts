import { signInWithEmailAndPassword } from './api.utils';

export type ObjectToAdd = {
  title: string;
};


export type AdditionalInformation = {
  displayName?: string;
};

export type UserData = {
  createdAt: Date;
  displayName: string;
  email: string;
};

export type User = {
    data: UserData;
};

export const signInAuthUserWithEmailAndPassword = async (email: string, password: string) => {
  if (!email || !password) return;

  return await signInWithEmailAndPassword(email, password);
};

export const signOutUser = async () => await signOut();

const signOut = async () => { return null };



export const getCurrentUser = (): Promise<UserData | null> => {
  return new Promise((resolve, reject) => {
      //TODO get user from global state
  });
};
