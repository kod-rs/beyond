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

        const response = await api.post(`csrf/`, JSON.stringify({ access_token, refresh_token, action: "csrf;select synchronizer_token" }));
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

        const response = await api.post(`locations/`, JSON.stringify({ access_token, refresh_token, action: "locations;delete single", index: i }));
        return await handleNewResponse(response);

    }

}

async function getLocationsFilterUsername() {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({ access_token, refresh_token, action: "locations;select username" }));
        return await handleNewResponse(response);

    }

}


async function getAllLocations() {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({ access_token, refresh_token, action: "locations;select_all" }));
        return await handleNewResponse(response);

    }

}

// async function getPortfolioUsername() {

//     const r = checkTokens()

//     if (r["status"]) {

//         let access_token = r["access_token"]
//         let refresh_token = r["refresh_token"]

//         const response = await api.get(`portfolio/`, JSON.stringify({ access_token, refresh_token, action: "portfolio;select all" }));
//         return await handleNewResponse(response);

//     }

// }

async function addLocation(section, type, latitude, longitude, csrfToken) {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({
            access_token, refresh_token, action: "locations;create single",
            type, section, latitude, longitude, synchronizer_token: csrfToken
        }));
        return await handleNewResponse(response);

    }

}


async function login(username, password) {

    const response = await api.post(`login/`, JSON.stringify({ username, password, action: "login;__comm" }))
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

        api.post(`logout/`, JSON.stringify({ access_token, refresh_token, action: "logout;__comm" }))

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

async function makeBackendRequest({ method, url, action, params }) {
    console.log("make backend req")
    const r = checkTokens()

    console.log("params", params)
    console.log("action", action)

    if (r["status"]) {

        let access_token = r["access_token"];
        let refresh_token = r["refresh_token"];

        if (method === "get") {

            return await handleNewResponse(
                await api.get(
                    url,
                    JSON.stringify({
                        access_token,
                        refresh_token,
                        action
                    })
                )
            );

        } else if (method === "post") {
            return await handleNewResponse(
                await api.post(
                    url,
                    JSON.stringify({
                        access_token,
                        refresh_token,
                        action
                    })
                )
            );

        }

    }


}

export const apiCalls = {
    makeBackendRequest,
    logout,
    login,
    getAllLocations,
    deleteLocation,
    getCSRFAuthData,
    addLocation,
    getCoordinates,
    getLocationsFilterUsername
}
