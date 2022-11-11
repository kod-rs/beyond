
export const signInWithEmailAndPassword = async (email: string, password: string) => {
    console.log('signInWithEmailAndPassword: ' + email + " " + password);

    //TODO Get base url from config
    const configURL = 'http://127.0.0.1:8000';

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };

    const res = await fetch(configURL + "/login/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    });

    let data = await res.json();
    console.log(data);
    return data;
};

