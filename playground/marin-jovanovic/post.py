import json

import requests


def login():
    url = 'http://127.0.0.1:8000/login/'
    data = {
        # "username": "Tracey_Ramos",
        "username": "Tracey_Ramosfff",
        "password": "lhecqksgih"
    }

    t = requests.post(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def keycloak_list_users():
    url = 'http://localhost:8080/admin'
    data = {
        # "grant_type": "password",
        # "client_id": "myclient",
        # "username": "myuser",
        # "password": "myuser"
    }

    t = requests.get(url, data=data, verify=False)
    print(t)
    print(t.text)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def keycloak_obtain_token():

    # url = 'http://localhost:8080/realms/myuser/protocol/openid-connect/token'
    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/token"
    data = {
        "grant_type": "password",
        "client_id": "beyond_cli",
        "username": "mirko",
        "password": "mirko"
        # "username": "user1",
        # "password": "user1"
    }

    t = requests.post(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def keycloak_logout():
    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/token"
    data = {
        # "grant_type": "password",
        "client_id": "beyond_cli",
        # todo nek ovo ide load iz konfig kad se starta app i nakon prvog poziva
        #   nek ide iz neke varijable
        "client_secret": "QDLsAp5bhXnIO98V90jwxcKMWyOaqYV_VefBGvAFZV4",
        # todo ovo ne smije bit access token nego iskljucivo refresh token
        "refresh_token": "2"
        # "username": "mirko",
        # "password": "mirko"
        # "username": "user1",
        # "password": "user1"
    }

    t = requests.post(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def keycloak_nekiget():
    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/token"
    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/certs"

    data = {
        # # "grant_type": "password",
        # "client_id": "beyond_cli",
        # "client_secret": "1",
        # # todo ovo ne smije bit access token nego iskljucivo refresh token
        # "refresh_token": "2"
        # # "username": "mirko",
        # # "password": "mirko"
        # # "username": "user1",
        # # "password": "user1"
    }

    t = requests.get(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def keycloak_api_login():
    url = "http://127.0.0.1:8000/auth/login/usr1/"
    data = {
        "name": "begin"
    }

    t = requests.post(url, data=data, verify=False)
    print(t)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def main():
    # keycloak_list_users()
    # keycloak_obtain_token()
    # keycloak_nekiget()
    # login()
    keycloak_api_login()


if __name__ == '__main__':
    main()
