
export const signInWithEmailAndPassword = async (email: string, password: string) => {
    console.log('signInWithEmailAndPassword: ' + email + " " + password);
    const configURL = 'http://127.0.0.1:8000';

    const bodyObj = {
        "type": "login_request",
        "username": email,
        "password": password
    };
    
    fetch(configURL+"/login/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bodyObj),
    })
        .then(data => {
            console.log(data);
            data.json();
        })
        .then(data => {
            if (data !== undefined) {
                console.log(data);
            } else {
                let mockData = {
                    "user": {
                        "type": "login_response",
                        "status": true,
                        "user_id": "edd2e5bc-1607-43c3-89f5-91b168be42b3",
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5M2RiODA4MC04NjI0LTQ1YTgtOTBhZi0xMjgwNDhiYjNiNmQifQ.eyJleHAiOjE2Njc4MjAyNjcsImlhdCI6MTY2NzgxODQ2NywianRpIjoiM2UwZTU1MTEtNjljZi00OWE3LTk3NmYtMTgyMjNiZTJjZWYzIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9CZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL0JleW9uZCIsInN1YiI6ImVkZDJlNWJjLTE2MDctNDNjMy04OWY1LTkxYjE2OGJlNDJiMyIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJCZXlvbmRDbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiODM3YjBmNWItNmEzZi00MDU4LWFhMGQtNmZjMTI0YWUxYTBhIiwic2NvcGUiOiJyb2xlcyBwcm9maWxlIGVtYWlsIiwic2lkIjoiODM3YjBmNWItNmEzZi00MDU4LWFhMGQtNmZjMTI0YWUxYTBhIn0.3NuWg-WqLEbhSBT_P04MXFuoSvHit8M29754G_p5_Ts"
                    }
                };
                return mockData;
            }
            return data;
        });

};