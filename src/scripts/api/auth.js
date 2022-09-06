import { apiCalls } from './comm';

async function login(username, password) {

    const response = await apiCalls.api.post(
        "login/",
        { action: "action tmp" },
        {
            headers: {
                'Authorization': 'Basic ' + ((encodeURIComponent(username + ':' + password)))
            }
        }
    );

    const user = await apiCalls.handleNewResponse(response)
    if (user) {
        console.log("setting user", user)
        sessionStorage.setItem('user', JSON.stringify(user));
    }
    return user

}

function logout() {
    if (sessionStorage.getItem("user") !== null) {
        apiCalls.api.post(
            "logout/",
            { action: "logout;__comm" },
            apiCalls.get_auth_header()
        );
        sessionStorage.removeItem('user');

    }

}

export const apiAuth = {
    login,
    logout
}