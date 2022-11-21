import { UserData } from "../../store/user/user.types";


//TODO Get base url from config
const configURL = 'http://127.0.0.1:8000';

export const signInWithEmailAndPassword = async (email: string, password: string) => {

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };

    const res = await fetch(configURL + "/login/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    console.log(data);
    return data;
};


export const getBuildingsForUser = async (user: UserData) => {
 
    const bodyObj = {
        "type": "buildings_by_user_id_request",
        "user_id": user.user_id,
    };

    const res = await fetch(configURL + "/buildings/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    console.log(data);
    return data;
};
