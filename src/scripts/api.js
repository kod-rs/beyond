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

    return await handleNewResponse(
        await api.post(
            "csrf/",
            {},
            get_auth_header()
        )
    );


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


async function addLocation(section, type, latitude, longitude, csrfToken) {

    return await handleNewResponse(
        await api.post(
            "locations/",
            JSON.stringify({

                type, section, latitude, longitude, synchronizer_token: csrfToken
            }),
            get_auth_header()
        )
    );


}


async function login(username, password) {

    const response = await api.post(
        "login/",
        { action: "action tmp" },
        {
            headers: {
                'Authorization': 'Basic ' + ((encodeURIComponent(username + ':' + password)))
            }
        }
    );

    const user = await handleNewResponse(response)
    if (user) {
        console.log("setting user", user)
        sessionStorage.setItem('user', JSON.stringify(user));
    }
    return user

}

function get_auth_header() {
    if (sessionStorage.getItem("user") !== null) {
        let user = JSON.parse(window.sessionStorage.getItem('user'));
        let access_token = user["auth"]["access-token"]
        let refresh_token = user["auth"]["refresh-token"];

        // console.log(access_token)

        return { headers: { 'Authorization': 'Digest ' + ((encodeURIComponent(access_token + ':' + refresh_token))) } }
    } else {
        return { headers: { 'Authorization': 'Digest ' + ((encodeURIComponent("not" + ':' + "present_err"))) } }
    }

}

function logout() {
    if (sessionStorage.getItem("user") !== null) {
        api.post(
            "logout/",
            { action: "logout;__comm" },
            get_auth_header()
        );
        sessionStorage.removeItem('user');

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

async function getCoordinates() {

    let response = await api.get(`https://ipapi.co/json/`)["data"];

    return {
        latitude: response["latitude"],
        longitude: response["longitude"]
    }

}


async function getLocationsFilterUsername() {

    return await handleNewResponse(
        await api.get(
            "locations/",
            get_auth_header()
        )
    );

}

async function getPortoflios() {

    return await handleNewResponse(
        await api.get(
            "portfolio/",
            get_auth_header()
        )
    );

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




export const apiCalls = {
    getPortoflios,
    logout,
    login,
    deleteLocation,
    getCSRFAuthData,
    addLocation,
    getCoordinates,
    getLocationsFilterUsername
}
