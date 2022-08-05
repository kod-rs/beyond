import api from './api';

export const userService = {
    login,
    logout,
    createOrUpdate,
    getAllLocations,
    addLocation,
    deleteLocation
};


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

async function addLocation(section, type, latitude, longitude) {

    const r = checkTokens()

    if (r["status"]) {

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        const response = await api.post(`locations/`, JSON.stringify({
            access_token, refresh_token, action: "add",
            type, section, latitude, longitude
        }));
        return await handleNewResponse(response);

    }

}


function login(username, password) {

    return api.post(`login/`, JSON.stringify({ username, password }))

        .then(handleNewResponse)
        .then(user => {
            if (user) {
                sessionStorage.setItem('user', JSON.stringify(user));
            }

            return user;
        });

}

function logout() {
    if (sessionStorage.getItem("user") !== null) {
        let user = JSON.parse(window.sessionStorage.getItem('user'));
        let access_token = user["auth"]["access-token"]
        const refresh_token = user["auth"]["refresh-token"]
        sessionStorage.removeItem('user');

        api.post(`logout/`, JSON.stringify({ access_token, refresh_token }))
            .then(r => {
                console.log("logout done")

            })
    }

}

function checkTokens() {

    console.log("check tokens")
    console.log()

    if (sessionStorage.getItem("user") !== null) {
        let user = JSON.parse(window.sessionStorage.getItem('user'));

        if (
            ("auth" in user) &&
            ("access-token" in user["auth"]) &&
            ("refresh-token" in user["auth"])
        ) {
            console.log("at & rt present")

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
