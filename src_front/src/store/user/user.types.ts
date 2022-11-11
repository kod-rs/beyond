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

export type AdditionalInformation = {
    displayName?: string;
};

export type User = {
    data: UserData;
};

export enum USER_TYPES {
    AGGREGATOR = 'Aggregator',
    MANAGER = 'Manager',
}

export type UserData = {
    message: string;
    status: boolean;
    type: string;
    user_id: string,
    access_token: string,
    displayName: string;
}
