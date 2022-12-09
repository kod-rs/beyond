/* Defining the type of action that is being dispatched. */
export enum USER_ACTION_TYPES {
    SET_CURRENT_USER = 'user/SET_CURRENT_USER',
    CHECK_USER_SESSION = 'user/CHECK_USER_SESSION',
    EMAIL_SIGN_IN_START = 'user/EMAIL_SIGN_IN_START',
    SIGN_IN_SUCCESS = 'user/SIGN_IN_SUCCESS',
    SIGN_IN_FAILED = 'user/SIGN_IN_FAILED',
    SIGN_OUT_START = 'user/SIGN_OUT_START',
    SIGN_OUT_SUCCESS = 'user/SIGN_OUT_SUCCESS',
    SIGN_OUT_FAILED = 'user/SIGN_OUT_FAILED',
}

/**
 * `User` is an object with a `data` property that is of type `UserData`.
 * @property {UserData} data - UserData;
 */
export type User = {
    data: UserData;
};

/* An enum that is used to define the type of user. */
export enum USER_TYPES {
    AGGREGATOR = 'Aggregator',
    MANAGER = 'Manager',
}

/**
 * UserData is an object with a message, status, type, user_id, access_token, and displayName property.
 * @property {string} message - string;
 * @property {boolean} status - boolean
 * @property {string} type - string;
 * @property {string} user_id - The user's unique ID.
 * @property {string} access_token - The access token that you can use to make API calls.
 * @property {string} displayName - The name of the user.
 */
export type UserData = {
    message: string;
    status: boolean;
    type: string;
    user_id: string,
    access_token: string,
    displayName: string;
}
