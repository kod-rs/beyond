import axios from 'axios'
import Cookies from 'js-cookie'

const api = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
})

async function getCSRFAuthData() {

    const r = checkTokens()

    const funRes = {
        "status": false,
        "synchronizer_token": undefined
    }

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"];

        const response = await api.post(`csrf/`, JSON.stringify({ access_token, refresh_token, action: "generate" }));
        const responseData = await handleNewResponse(response)["payload"];

        funRes["synchronizer_token"] = responseData["synchronizer_token"];
        funRes["status"] = true;

    }

    return funRes;

}

async function deleteLocation(i) {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({ access_token, refresh_token, action: "delete", index: i }));
        // const response = await api.get(`locations/`, JSON.stringify({ access_token, refresh_token }));
        return await handleNewResponse(response);

    }

}

async function getAllLocations() {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({ access_token, refresh_token, action: "get all" }));
        // const response = await api.get(`locations/`, JSON.stringify({ access_token, refresh_token }));
        return await handleNewResponse(response);

    }

}

async function addLocation(section, type, latitude, longitude, csrfToken) {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({
            access_token, refresh_token, action: "add",
            type, section, latitude, longitude, synchronizer_token: csrfToken
        }));
        return await handleNewResponse(response);

    }

}


async function login(username, password) {

    const response = await api.post(`login/`, JSON.stringify({ username, password }))
    const user = await handleNewResponse(response)
    if (user) {
        sessionStorage.setItem('user', JSON.stringify(user))
    }
    return user

}

function logout() {
    if (sessionStorage.getItem("user") !== null) {
        let user = JSON.parse(window.sessionStorage.getItem('user'));
        let access_token = user["auth"]["access-token"]
        const refresh_token = user["auth"]["refresh-token"]
        sessionStorage.removeItem('user');

        api.post(`logout/`, JSON.stringify({ access_token, refresh_token }))
        // .then(r => {

        // })
    }

}

function checkTokens() {


    if (sessionStorage.getItem("user") !== null) {
        let user = JSON.parse(window.sessionStorage.getItem('user'));

        if (
            ("auth" in user) &&
            ("access-token" in user["auth"]) &&
            ("refresh-token" in user["auth"])
        ) {

            const access_token = user["auth"]["access-token"]
            const refresh_token = user["auth"]["refresh-token"]

            return {
                "status": true,
                "access_token": access_token,
                "refresh_token": refresh_token
            }

        }

    }

    return {
        "status": false
    }


}

async function getAllTest() {
    const r = checkTokens()
    if (r["status"]) {
        let access_token = r["access-token"]
        const refresh_token = r["refresh-token"]

        const response = await api.put(`getAll/`, JSON.stringify({ access_token, refresh_token }));
        let r2 = await handleNewResponse(response);
        return r2;

    }
}

async function createOrUpdate(id, newValue) {
    const r = checkTokens()
    if (r["status"]) {
        let access_token = r["access-token"]
        let refresh_token = r["refresh-token"]

        const response = await api.put(`testcrud/`, JSON.stringify({ access_token, refresh_token, id, newValue }));
        return await handleNewResponse(response);

    }

}


function handleNewResponse(response) {

    if (!response.data.auth.status) {
        if (response.data.status === 401) {
            logout();
            location.reload(true);
        }

        const error = "username password combination mismatchrr"
        return Promise.reject(error);
    }

    return response.data
}

async function getCoordinates() {

    let response = await api.get(`https://ipapi.co/json/`)
    response = response["data"]
    return {
        latitude: response["latitude"],
        longitude: response["longitude"]
    }

}

export const apiCalls = {
    logout,
    login,
    getAllLocations,
    deleteLocation,
    getCSRFAuthData,
    addLocation,
    getCoordinates
}