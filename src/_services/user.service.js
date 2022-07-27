import api from './api';

export const userService = {
    login,
    logout,

};


function login(username, password) {


    return api.post(`login/`, JSON.stringify({ username, password }))

        .then(handleNewResponse)
        .then(user => {
            if (user) {
                localStorage.setItem('user', JSON.stringify(user));
            }

            return user;
        });



}

function logout() {
    if (localStorage.getItem("user") !== null) {
        let user = JSON.parse(window.localStorage.getItem('user'));
        let access_token = user["auth"]["access-token"]
        const refresh_token = user["auth"]["refresh-token"]
        localStorage.removeItem('user');

        api.post(`logout/`, JSON.stringify({ access_token, refresh_token }))
            .then(r => {
                console.log("logout done")

            })
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
