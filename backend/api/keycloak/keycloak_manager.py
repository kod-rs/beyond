import json

import jwt
import requests
from decouple import config

from backend.api.keycloak.keys_manager import get_all_keys, remove_key


def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))


def get_links():
    base = config("KEYCLOAK_URL")

    links = {
        "authorization-uri": base + "auth",
        "user-info-uri": base + "userinfo",
        "token-uri": base + "token",
        "logout": base + "logout",
        "jwk-set-uri": base + "certs"
    }

    return links


def get_con():
    return {
        "realm": config("KEYCLOAK_REALM"),
        "client id": config("KEYCLOAK_CLIENT_ID"),
        "authorization grant type": "password",
        "client secret": config("KEYCLOAK_CLIENT_SECRET"),
        "scope": "openid profile"
    }


def get_roles(access_token):
    keys = get_all_keys()
    if keys["status"]:

        for k_type, k in keys["payload"]:
            try:
                jwt_ = jwt.decode(
                    access_token,
                    key=k,
                    algorithms=[k_type]
                )
            except jwt.exceptions.InvalidAlgorithmError:
                print("removing", k_type)
                remove_key(k_type)
                continue

            return jwt_["resource_access"][get_con()["client id"]]["roles"]

    else:
        print("no keys")


def keycloak_obtain_token(username, password):
    url = get_links()["token-uri"]

    data = {
        "username": username,
        "password": password,
        "client_id": get_con()["client id"],
        "grant_type": get_con()["authorization grant type"],
        "client_secret": get_con()["client secret"],
        "scope": get_con()["scope"]
    }

    res = requests.post(url, data=data, verify=False)

    res_text = json.loads(res.text)

    return res_text


def logout(refresh_token):
    url = get_links()["logout"]

    data = {

        "client_id": get_con()["client id"],
        "client_secret": get_con()["client secret"],
        "refresh_token": refresh_token

    }

    res = requests.post(url, data=data, verify=False)

    if res.status_code == 204:
        print("ok")
        return True
    else:
        print("err")
        return False


def get_user_info(token):
    url = get_links()["user-info-uri"]

    headers = {
        "Authorization": "bearer " + token
    }

    res = requests.post(url, headers=headers, verify=False)

    res_text = json.loads(res.text)

    return res_text


def is_valid(token):
    res = get_user_info(token)
    if all((i in res) for i in ["email_verified", "preferred_username", "sub"]):
        return True
    elif all((i in res) for i in ["error", "error_description"]):
        return False
    else:
        return False

def try_refresh_token(token):
    url = get_links()["token-uri"]
    # print("url", url)

    headers = {
        "Authorization": "bearer " + token
    }

    body = {
        "client_id": config("KEYCLOAK_CLIENT_ID"),
        "grant_type": "refresh_token",
        "refresh_token": token,
        "client_secret": get_con()["client secret"],

    }

    res = requests.post(url, data=body, verify=False)

    res_text = json.loads(res.text)

    return res_text

def main():

    access_token = config["access_token"]
    refresh_token = config["refresh_token"]

    print(f"{is_valid(access_token)=}")

    t = try_refresh_token(refresh_token)
    print(t)



    # res = keycloak_obtain_token("mirko", "mirko")
    # pretty_print_json(res)
    # access_token = res["access_token"]
    # refresh_token = res["refresh_token"]
    #
    # roles = get_roles(res["access_token"])
    # print(f"{roles=}")
    #
    # print(f"{is_valid(access_token)=}")

    #
    # res = get_user_info(access_token)
    # print(res)
    #
    # print(f"{is_valid('fake token')=}")
    #
    # print("logout")
    # print(f"{logout(refresh_token)=}")
    #
    # print(f"{is_valid(access_token)=}")
    # print(f"{is_valid('fake token')=}")


if __name__ == '__main__':
    main()
