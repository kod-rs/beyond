import { AnyAction } from 'redux';
import { Algorithm_Response, Flexibility_Offer_Confirmation_Response } from './algorithm.types';
import {  
    getAlgorithmDataFailed,
    getAlgorithmDataSuccess,
    sendFlexOfferSuccess,
    sendFlexOfferFailed,
    setAlgorithmDataLoading,
} from './algorithm.action';


/**
 * AlgorithmDataState is an object with the following properties: algorithmData,
 * offer_confirmation_response, isLoading, and error. Each of these properties is either a nullable
 * Algorithm_Response, Flexibility_Offer_Confirmation_Response, boolean, or Error.
 * @property {Algorithm_Response | null} algorithmData - Algorithm_Response | null;
 * @property {Flexibility_Offer_Confirmation_Response | null} offer_confirmation_response -
 * Flexibility_Offer_Confirmation_Response | null;
 * @property {boolean} isLoading - boolean;
 * @property {Error | null} error - Error | null;
 */
export type AlgorithmDataState = {
    readonly algorithmData: Algorithm_Response | null;
    readonly offer_confirmation_response: Flexibility_Offer_Confirmation_Response | null;
    readonly isLoading: boolean;
    readonly error: Error | null;
};

/* Setting the initial state of the reducer. */
const INITIAL_STATE: AlgorithmDataState = {
    algorithmData: null,
    offer_confirmation_response:null,
    isLoading: false,
    error: null,
};

/**
 * If the action matches the action type, then return the state with the new data, otherwise return the
 * state.
 * @param state - The current state of the reducer.
 * @param action - {type: "GET_ALGORITHM_DATA_SUCCESS", payload: {…}}
 * @returns The state is being returned.
 */
export const algorithmDataReducer = (
  state = INITIAL_STATE,
  action = {} as AnyAction
) => {
    if (getAlgorithmDataSuccess.match(action)) {
        return { ...state, algorithmData: action.payload, isLoading:false };
    }

    if (getAlgorithmDataFailed.match(action)) {
        return { ...state, error: action.payload, isLoading: false };
    }

    if (sendFlexOfferSuccess.match(action)) {
        return { ...state, offer_confirmation_response: action.payload, isLoading: false };
    }

    if (sendFlexOfferFailed.match(action)) {
        return { ...state, error: action.payload, isLoading: false };
    }

    if (setAlgorithmDataLoading.match(action)) {
        return { ...state, isLoading: action.payload };
    }

  return state;
};
