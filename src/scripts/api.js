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

async function getCoordinates() {

    let response = await api.get(`https://ipapi.co/json/`)["data"];

    return {
        latitude: response["latitude"],
        longitude: response["longitude"]
    }

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

async function createOrUpdatePortfolio(currentName, newName, colour) {
    // todo csrf

    return await handleNewResponse(
        await api.post(
            "portfolio/",
            JSON.stringify({
                currentName,
                newName
                , colour

            }),
            get_auth_header()
        )
    );
}

async function deletePortfolio(currentName,) {
    // todo csrf

    return await handleNewResponse(
        await api.delete(
            "portfolio/" + currentName,
            get_auth_header()
        )
    );
}



export const apiCalls = {
    api,
    handleNewResponse,
    get_auth_header,

    deletePortfolio,
    createOrUpdatePortfolio,
    getPortoflios,
    logout,
    login,
    getCSRFAuthData,
    getCoordinates,
}
