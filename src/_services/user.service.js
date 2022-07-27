import api from './api';

export const userService = {
    login,
    logout,

};


function login(username, password) {
    const headers = {
        // 'username': username,
        // "password": password,
        // 'Content-Type': 'application/json;charset=UTF-8',
        // "Access-Control-Allow-Origin": "*",
        // "Access-Control-Allow-Origin": "*",
        // "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
        // "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization",
    }

    return api.post(`login/`, JSON.stringify({ username, password }), { headers: headers })
        // return api.post(`/login`, JSON.stringify({ username, password }), { headers: headers })

        .then(handleNewResponse)
        .then(user => {
            if (user) {
                localStorage.setItem('user', JSON.stringify(user));
            }

            return user;
        });


    // return await fetch(url, {
    //     method: 'POST', // *GET, POST, PUT, DELETE, etc.
    //     mode: 'cors', // no-cors, *cors, same-origin
    //     cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    //     credentials: 'same-origin', // include, *same-origin, omit
    //     headers: {
    //       'Content-Type': 'application/json'
    //       // 'Content-Type': 'application/x-www-form-urlencoded',
    //     },
    //     redirect: 'follow', // manual, *follow, error
    //     referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    //     body: JSON.stringify(data) // body data type must match "Content-Type" header
    //   });
    //   return response.json(); // parses JSON response into native JavaScript objects

}

function logout() {
    localStorage.removeItem('user');
    /*
        return api.post(`logout/`, JSON.string   ify({ username, password }))
            .then(handleNewResponse)
            .then(user => {
                if (user) {
                    localStorage.setItem('user', JSON.stringify(user));
                }
    
                return user;
            });
    */
}

function handleNewResponse(response) {
    console.log(response)

    response = response.data

    console.log(response)

    // if (!response.ok) {
    if (!response.auth.status) {
        if (response.status === 401) {
            logout();
            location.reload(true);
        }

        const error = "username password combination mismatchrr"
        return Promise.reject(error);
    }
    return response
}

// function handleResponse(response) {

//     return response.text().then(text => {
//         const data = text && JSON.parse(text);
//         if (!response.ok) {
//             if (response.status === 401) {
//                 logout();
//                 location.reload(true);
//             }

//             //  const error = (data && data.message) || response.statusText;

//             return Promise.reject(error);
//         }

//         return data;
//     });
// }