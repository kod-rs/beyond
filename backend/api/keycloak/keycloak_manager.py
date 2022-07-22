import json
import os
import sys

import requests
from decouple import config
import jwt
import pem

def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))


def get_links():
    base = f"http://localhost:8080/realms/{get_con()['realm']}/protocol/openid-connect/"
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
        "realm": "beyond",
        "client id": "beyond_cli",
        "authorization grant type": "password",

        "client secret": config("client_secret"),
        "scope": "openid profile"
    }



def get_roles(access_token):
    # url = "http://localhost:8080/realms/beyond/protocol/openid-connect/certs"
    # res = requests.get(url, verify=False)
    # res_text = json.loads(res.text)
    # # print(res_text)
    #
    # public_key = None
    # for k in res_text["keys"]:
    #     if k["alg"] == "RS256":
    #         public_key = k["n"]
    #         print(public_key)
    #

    # pem.generate_keys()

    current_folder = pathlib.Path(__file__).parent.resolve()

    keys = ["RS256", "RSA-OAEP"]


    for k in keys:

        with open(current_folder / f"{k}.key") as f:
            l = f.read()

            t = jwt.decode(access_token, key=l,algorithms=["RS256"])
            # print(t)


    sys.exit(-1)

    # header = jwt.get_unverified_header(access_token)
    t = jwt.decode(access_token, options={"verify_signature": False})
    t = t["resource_access"]
    t = t["beyond_cli"]
    t = t["roles"]
    # sys.exit(-1)

    return t

# def keycloak_obtain_token(username="mirko", password="mirko"):
def keycloak_obtain_token(username="user1", password="p"):

    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/token"

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

    pretty_print_json(res_text)

    return res_text

def is_valid(token):
    res = get_user_info(token)
    if all((i in res) for i in ["email_verified", "preferred_username", "sub"]):
        print("login true")
        return True
    elif all((i in res) for i in ["error", "error_description"]):
        print("login false")
        return False
    else:
        print("other err")



def main():
    # print("login")
    res = keycloak_obtain_token()
    print("login res", res)

    roles = get_roles(res["access_token"])
    print(f"{roles=}")

    access_token = res["access_token"]
    refresh_token = res["refresh_token"]
    # print(access_token)

    print("check valid")
    print(f"{is_valid(access_token)=}")

    print(80 * "_")

    res = get_user_info(access_token)
    print(res)

    print(f"{is_valid('fake token')=}")

    print("logout")
    res = logout(refresh_token)

    print(f"{is_valid(access_token)=}")

    # res = check_validity(access_token)
    # res = check_validity("access_token")

if __name__ == '__main__':
    main()