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
    localStorage.removeItem('user');
}

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
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}