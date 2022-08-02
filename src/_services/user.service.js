import api from './api';

export const userService = {
    login,
    logout,
    createOrUpdate,
    getAllLocations
};

async function getAllLocations(aT, rT) {

    const r = checkTokens()
    console.log(2)
    if (r["status"]) {
        console.log(3)

        let access_token = r["access_token"]
        let refresh_token = r["refresh_token"]

        console.log(1)
        // if ((localStorage.getItem("user") !== null) &&
        //     ("auth" in user) &&
        //     ("access-token" in user["auth"]) && 
        //     ("refresh-token" in user["auth"])
        // ) {
        //     let user = JSON.parse(window.localStorage.getItem('user'));
        //     let access_token = user["auth"]["access-token"]
        //     const refresh_token = user["auth"]["refresh-token"]



        const response = await api.put(`locations/`, JSON.stringify({ access_token, refresh_token }));
        const r = await handleNewResponse(response);
        return r;

    }

    // console.log("locat")
    // console.log("ffff")
    // const r = checkTokens()
    // console.log(r)
    // console.log(3)

    // if (r["status"]) {
    //     console.log(2)
    //     let access_token = r["access-token"]
    //     const refresh_token = r["refresh-token"]

    //     console.log(1)

    //     const response = await api.get(`locations/`, JSON.stringify({ access_token, refresh_token }));
    //     console.log("response", response)
    //     let r2 = await handleNewResponse(response);
    //     return r2;

    // } else {
    //     console.log("status false")
    // }

}



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

function checkTokens() {

    console.log("check tokens")
    console.log()

    if (localStorage.getItem("user") !== null) {
        let user = JSON.parse(window.localStorage.getItem('user'));

        if (("auth" in user) &&
            ("access-token" in user["auth"]) &&
            ("refresh-token" in user["auth"])
        ) {
            console.log("have evertythin")

            // let user = JSON.parse(window.localStorage.getItem('user'));
            const access_token = user["auth"]["access-token"]
            const refresh_token = user["auth"]["refresh-token"]

            // console.log(access_token)
            // console.log(refresh_token)

            return {
                "status": true,
                "access_token": access_token,
                "refresh_token": refresh_token
            }

        }

    }

    return {
        "status": true
    }


    // if ((window.localStorage.getItem("user") !== null) &&
    //     ("auth" in localStorage.getItem("user")) &&
    //     ("access-token" in localStorage.getItem("user")["auth"]) &&
    //     ("refresh-token" in localStorage.getItem("user")["auth"])
    // ) {
    //     console.log("have evertythin")

    //     let user = JSON.parse(window.localStorage.getItem('user'));
    //     let access_token = user["auth"]["access-token"]
    //     const refresh_token = user["auth"]["refresh-token"]

    //     return {
    //         "status": true,
    //         "access_token": access_token,
    //         "refresh_token": refresh_token
    //     }
    // } else {
    //     console.log("local storage missing")

    //     return {
    //         "status": true
    //     }
    // }

    // console.log("other")
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
        const refresh_token = r["refresh-token"]


        // if ((localStorage.getItem("user") !== null) &&
        //     ("auth" in user) &&
        //     ("access-token" in user["auth"]) && 
        //     ("refresh-token" in user["auth"])
        // ) {
        //     let user = JSON.parse(window.localStorage.getItem('user'));
        //     let access_token = user["auth"]["access-token"]
        //     const refresh_token = user["auth"]["refresh-token"]



        const response = await api.put(`testcrud/`, JSON.stringify({ access_token, refresh_token, id, newValue }));
        const r = await handleNewResponse(response);
        return r;

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
