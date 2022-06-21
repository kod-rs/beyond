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
    url = 'http://localhost:8080/realms/myuser/protocol/openid-connect/token'
    data = {
        "grant_type": "password",
        "client_id": "myclient",
        "username": "myuser",
        "password": "myuser"
    }

    t = requests.post(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def main():
    keycloak_list_users()

if __name__ == '__main__':
    main()
