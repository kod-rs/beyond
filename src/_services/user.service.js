import config from 'config';
import api from './api'

export const userService = {
    login,
    logout,

};


function login(username, password) {

    return api.post(`login/`, JSON.stringify({ username, password }))
        .then(handleNewResponse)
        .then(user => {
            if (user) {
                // user.authdata = window.btoa(username + ':' + password);
                localStorage.setItem('user', JSON.stringify(user));
            }

            return user;
        });

}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

// function getAll() {
//     const requestOptions = {
//         method: 'GET',
//         headers: authHeader()
//     };

// export function authHeader() {
//     // return authorization header with basic auth credentials
//     let user = JSON.parse(localStorage.getItem('user'));

//     if (user && user.authdata) {
//         return { 'Authorization': 'Basic ' + user.authdata };
//     } else {
//         return {};
//     }
// }

//     return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
// }

function handleNewResponse(response) {
    response = response.data

    if (!response.ok) {
        if (response.status === 401) {
            logout();
            location.reload(true);
        }

        const error = "err"
        return Promise.reject(error);
    }
    return response
}

function handleResponse(response) {

    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}