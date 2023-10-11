import { Algorithm_Request, Algorithm_Response } from "../../store/algorithm/algorithm.types";
import { Building } from "../../store/buildings/buildings.types";
import { UserData } from "../../store/user/user.types";

/* A constant that is being used to store the base URL of the API. */
const CONFIG_URL = process.env.REACT_APP_BASE_URL;

/* Defining an enumeration of strings. */
enum REQUEST_TYPES {
    LOGIN_REQUEST = "/login/",
    BUILDINGS_REQUEST = "/buildings/",
    FLEX_DEMAND_REQUEST = "/flexibility_demand/",
    ALGORITHM_REQUEST = "/algorithm/",
    SEND_FLEX_OFFER_REQUEST = "/flexibility_offer_confirmation/",
}


/**
 * This function takes in a request type and a body object, and returns a promise that resolves to the
 * data returned from the server.
 * @param {REQUEST_TYPES} request_type - REQUEST_TYPES = 'login' | 'register' | 'logout' |
 * 'get_user_data' | 'update_user_data' | 'delete_user_data'
 * @param {object} bodyObj - {
 * @returns The data is being returned as a promise.
 */
const call_Fetch_Post = async (request_type: REQUEST_TYPES, bodyObj:object) => {
    const res = await fetch(request_type, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    return data;
}

/**
 * This function takes in an email and password, and returns a promise that resolves to a response
 * object.
 * @param {string} email - string, password: string
 * @param {string} password - string
 * @returns The data is being returned from the call_Fetch_Post function.
 */
export const signInWithEmailAndPassword = async (email: string, password: string) => {

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.LOGIN_REQUEST, bodyObj);
    return data;
};


/**
 * This function takes a user object, and returns a promise that resolves to an array of building
 * objects.
 * @param {UserData} user - UserData = {
 * @returns {
 *     "type": "buildings_by_user_id_response",
 *     "buildings": [
 *         {
 *             "building_id": "1",
 *             "building_name": "Building 1",
 *             "building_address": "123 Main St",
 *             "building_city": "Anytown",
 *             "building_state
 */
export const getBuildingsForUser = async (user: UserData) => {
 
    const bodyObj = {
        "type": "buildings_by_user_id_request",
        "user_id": user.user_id,
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.BUILDINGS_REQUEST, bodyObj);
    return data;
};

/**
 * This function takes an array of buildings, and returns an array of buildings with additional data.
 * @param {Building[]} buildings - Building[]
 */
export const getBuildingHistoryData = async (buildings: Building[]) => {

    const bodyObj = {
        "type": "building_info_request",
        "building_ids": buildings.map((building) => building.building_id),
        // "resolution": "day"  TODO add logic to fetch resolution
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.BUILDINGS_REQUEST, bodyObj);
    return data;
};

/**
 * This function takes a date as an argument and returns a promise that resolves to an object
 * containing the data from the API call.
 * @param {Date} date - Date
 */
export const getFlexDemandData = async (date: Date) => {

    const bodyObj = {
        "type": "flexibility_demand_request",
        "date": date.toISOString(), //RFC 3339 format 
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.FLEX_DEMAND_REQUEST, bodyObj);
    return data;
};

/**
 * It takes an object of type Algorithm_Request, converts it to a JSON object, and sends it to the
 * server.
 * @param {Algorithm_Request} request - Algorithm_Request
 * @returns The data is being returned as a string.
 */
export const getAlgorithmData = async (request: Algorithm_Request) => {

    const bodyObj = {
        "type": "algorithm_request",
        "building_energy_list": request.building_energy_list,
        "flexibility_demands": request.flexibility_demands,
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.ALGORITHM_REQUEST, bodyObj);
    return data;
};

/**
 * It takes a user_id and an algorithm_response object, and sends a POST request to the server with the
 * user_id and algorithm_response object as the body
 * @param {string} user_id - string, response: Algorithm_Response
 * @param {Algorithm_Response} response - Algorithm_Response
 * @returns The response from the server.
 */
export const sendFlexOffer = async (user_id: string, response: Algorithm_Response) => {

    const bodyObj = {
        "type": "flexibility_offer_confirmation_request",
        "user_id": user_id,
        "algorithm_response": response,
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.SEND_FLEX_OFFER_REQUEST, bodyObj);
    return data;
};
