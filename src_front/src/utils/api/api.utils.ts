import { Algorithm_Request } from "../../store/algorithm/algorithm.types";
import { Building } from "../../store/buildings/buildings.types";
import { UserData } from "../../store/user/user.types";

const CONFIG_URL = process.env.REACT_APP_BASE_URL;

enum REQUEST_TYPES {
    LOGIN_REQUEST = "/login/",
    BUILDINGS_REQUEST = "/buildings/",
    FLEX_DEMAND_REQUEST = "/flexibility_demand/",
    ALGORITHM_REQUEST = "/algorithm/",
}


const call_Fetch_Post = async (request_type: REQUEST_TYPES, bodyObj:object) => {
    const res = await fetch(CONFIG_URL + request_type, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    return data;
}

export const signInWithEmailAndPassword = async (email: string, password: string) => {

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.LOGIN_REQUEST, bodyObj);
    return data;
};


export const getBuildingsForUser = async (user: UserData) => {
 
    const bodyObj = {
        "type": "buildings_by_user_id_request",
        "user_id": user.user_id,
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.BUILDINGS_REQUEST, bodyObj);
    return data;
};

export const getBuildingHistoryData = async (buildings: Building[]) => {

    const bodyObj = {
        "type": "building_info_request",
        "building_ids": buildings.map((building) => building.building_id)
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.BUILDINGS_REQUEST, bodyObj);
    return data;
};

export const getFlexDemandData = async (date: Date) => {

    const bodyObj = {
        "type": "flexibility_demand_request",
        "date": date.toISOString(), //RFC 3339 format 
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.FLEX_DEMAND_REQUEST, bodyObj);
    return data;
};

export const getAlgorithmData = async (request: Algorithm_Request) => {

    const bodyObj = {
        "type": "algorithm_request",
        "building_energy_list": request.building_energy_list,
        "interval": {
            "from": request.from.toISOString(), //RFC 3339 format
            "to": request.to.toISOString(), //RFC 3339 format
        },
        "flexibility_amount": request.amount,
    };

    let data = await call_Fetch_Post(REQUEST_TYPES.ALGORITHM_REQUEST, bodyObj);
    return data;
};
