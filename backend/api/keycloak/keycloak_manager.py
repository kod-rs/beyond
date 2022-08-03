import json

import jwt
import requests
from decouple import config

from backend.api.comm.comm import pretty_print_json
from backend.api.cqrs_c.pem_keys import remove_jwt_public_key
from backend.api.cqrs_q.pem_keys import get_all_keys
from backend.api.keycloak.config import get_urls, get_config
from backend.api.keycloak.pem import generate_keys


def get_roles(access_token):
    keys = get_all_keys()

    if not keys:
        generate_keys()
        print("keys not exist")
    else:
        print("keys exist")

    keys = get_all_keys()
    if not keys:
        print("no keys")
    else:

        for i in keys.iterator():
            k_type, k = i.key_type, i.key_value
            try:
                jwt_ = jwt.decode(
                    access_token,
                    key=k,
                    algorithms=[k_type]
                )
            except jwt.exceptions.InvalidAlgorithmError:
                print("removing", k_type)
                remove_jwt_public_key(k_type)
                continue

            except jwt.exceptions.DecodeError:
                print("error decoding")
                return []

            except jwt.exceptions.ExpiredSignatureError:
                print("refresh token dead?")
                return []

            if "resource_access" in jwt_:
                return jwt_["resource_access"][get_config()["client id"]][
                    "roles"]

            else:
                return []


def keycloak_obtain_token(username, password):
    url = get_urls()["token-uri"]

    data = {
        "username": username,
        "password": password,
        "client_id": get_config()["client id"],
        "grant_type": get_config()["authorization grant type"],
        "client_secret": get_config()["client secret"],
        "scope": get_config()["scope"]
    }

    res = requests.post(url, data=data, verify=False)

    res_text = json.loads(res.text)
    return res_text


def logout(refresh_token):
    url = get_urls()["logout"]

    data = {

        "client_id": get_config()["client id"],
        "client_secret": get_config()["client secret"],
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
    url = get_urls()["user-info-uri"]

    headers = {
        "Authorization": "bearer " + token
    }

    res = requests.post(url, headers=headers, verify=False)

    res_text = json.loads(res.text)

    return res_text


def is_valid(access_token, refresh_token):
    res = get_user_info(access_token)
    if all((i in res) for i in ["email_verified", "preferred_username", "sub"]):
        return {
            "is_valid": True,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "test is_current_valid": True
        }
    else:

        res = try_refresh_token(refresh_token)

        if all((i in res) for i in ["access_token", "refresh_token"]):

            return {
                "is_valid": True,
                "access_token": res["access_token"],
                "refresh_token": res["refresh_token"],
                "test is_current_valid": False
            }

        else:

            return {
                "is_valid": False
            }


def try_refresh_token(token):
    url = get_urls()["token-uri"]

    body = {
        "client_id": config("KEYCLOAK_CLIENT_ID"),
        "grant_type": "refresh_token",
        "refresh_token": token,
        "client_secret": get_config()["client secret"],

    }

    res = requests.post(url, data=body, verify=False)

    res_text = json.loads(res.text)

    return res_text


def main():
    res = keycloak_obtain_token("mirko", "mirko")
    pretty_print_json(res)
    print()
    access_token = res["access_token"]
    refresh_token = res["refresh_token"]

    # roles = get_roles(res["access_token"])
    # print(f"{roles=}")

    print("is valid")
    res = is_valid(access_token, refresh_token)
    pretty_print_json(res)
    print()
    access_token = res["access_token"]
    refresh_token = res["refresh_token"]

    # print(f"{is_valid(access_token, refresh_token)=}")

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
