import { Algorithm_Request } from "../../store/algorithm/algorithm.types";
import { Building } from "../../store/buildings/buildings.types";
import { Building_Info } from "../../store/historicData/historicData.types";
import { UserData } from "../../store/user/user.types";


//TODO Get base url from config
const CONFIG_URL = 'http://127.0.0.1:8000';

const LOGIN_REQUEST = "/login/";
const BUILDINGS_REQUEST  = "/buildings/";
const FLEX_DEMAND_REQUEST  = "/flexibility_demand/";
const ALGORITHM_REQUEST = "/algorithm/";

export const signInWithEmailAndPassword = async (email: string, password: string) => {

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };

    const res = await fetch(CONFIG_URL + LOGIN_REQUEST , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    //console.log(data);
    return data;
};


export const getBuildingsForUser = async (user: UserData) => {
 
    const bodyObj = {
        "type": "buildings_by_user_id_request",
        "user_id": user.user_id,
    };

    const res = await fetch(CONFIG_URL + BUILDINGS_REQUEST , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    //console.log(data);
    return data;
};

export const getBuildingHistoryData = async (buildings: Building[]) => {

    const bodyObj = {
        "type": "building_info_request",
        "building_ids": buildings.map((building) => building.building_id)
    };

    const res = await fetch(CONFIG_URL + BUILDINGS_REQUEST , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    //console.log(data);
    return data;
};

export const getFlexDemandData = async (date: Date) => {

    const bodyObj = {
        "type": "flexibility_demand_request",
        "date": date.toISOString()
    };

    const res = await fetch(CONFIG_URL + FLEX_DEMAND_REQUEST , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    //console.log(data);
    return data;
};

export const getAlgorithmData = async (request: Algorithm_Request) => {

    const bodyObj = {
        "type": "algorithm_request",
        "building_energy_list": request.building_energy_list,
        "interval": {
            "from": request.from.toISOString(),
            "to": request.to.toISOString(),
        },
        "flexibility_amount": request.amount,
    };

    const res = await fetch(CONFIG_URL + ALGORITHM_REQUEST , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    //console.log(data);
    return data;
};
