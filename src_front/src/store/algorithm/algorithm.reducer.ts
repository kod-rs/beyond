import { AnyAction } from 'redux';
import { Algorithm_Response, Flexibility_Offer_Confirmation_Response } from './algorithm.types';
import {  
    getAlgorithmDataFailed,
    getAlgorithmDataSuccess,
    sendFlexOfferSuccess,
    sendFlexOfferFailed
} from './algorithm.action';


export type AlgorithmDataState = {
    readonly algorithmData: Algorithm_Response | null;
    readonly offer_confirmation_response: Flexibility_Offer_Confirmation_Response | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

const INITIAL_STATE: AlgorithmDataState = {
    algorithmData: null,
    offer_confirmation_response:null,
    isLoading: false,
    error: null,
};

export const algorithmDataReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getAlgorithmDataSuccess.match(action)) {
        return { ...state, algorithmData: action.payload };
    }

    if (getAlgorithmDataFailed.match(action)) {
        return { ...state, error: action.payload };
    }

    if (sendFlexOfferSuccess.match(action)) {
        return { ...state, offer_confirmation_response: action.payload };
    }

    if (sendFlexOfferFailed.match(action)) {
        return { ...state, error: action.payload };
    }

  return state;
};
