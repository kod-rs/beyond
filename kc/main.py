import json
import requests
from decouple import config
import jwt


def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))

realm = "beyond"


def get_links():
    baselink = f"http://localhost:8080/realms/{realm}/protocol/openid-connect"
    links = {
        "authorization-uri": baselink + "/auth",
        "user-info-uri": baselink + "/userinfo",
        "token-uri": baselink + "/token",
        "logout": baselink + "/logout",
        "jwk-set-uri": baselink + "/certs"
    }

    return links

def get_con():

    return {
        "client id": "beyond_cli",
        "authorization grant type": "password",

        "client secret": config("client_secret"),
        "scope": "openid profile"
    }

def get_roles(access_token):
    print(80 * "#")
    t = jwt.decode(access_token, options={"verify_signature": False})
    t = t["resource_access"]
    # print(t)
    t = t["beyond_cli"]
    # print(t)
    t = t["roles"]
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

    pretty_print_json(res_text)

    # access_token = res_text["access_token"]
    # print(access_token)
    # header = jwt.get_unverified_header(access_token)
    # print(header)
    # [print(type(i)) for i in header]
    # print(header["alg"])
    # print(jwt.decode(access_token, options={"verify_signature": False}))
    # print(jwt.decode(access_token, algorithms=header["alg"]))
    # return
    # print(jwt.decode(access_token, header["kid"], algorithms=header["alg"]))

    # access_token = str(access_token).split(".", 1)
    # print(f"{access_token=}")
    # print(len(access_token))
    # print(access_token[1])

    # decoded = jwt.decode(str(access_token).split(".",1)[1], algorithms=decoded["alg"])
    # print(decoded)

    # decoded = jwt.decode(access_token, options={
    #     "verify_signature": True}, algorithms="RS256")  # works in PyJWT >= v2.0

    return res_text


def logout(refresh_token):
    url = get_links()["logout"]

    data = {
        # "username": username,
        # "password": password,
        "client_id": get_con()["client id"],
        # "grant_type": get_con()["authorization grant type"],
        "client_secret": get_con()["client secret"],
        "refresh_token": refresh_token

    }

    res = requests.post(url, data=data, verify=False)
    print(res)
    print(res.text)
    print(type(res))
    if res.status_code == 204:
        print("ok")
        return True
    else:
        print("err")
        return False

    # if res ==
    # res_text = json.loads(res.text)

    # pretty_print_json(res_text)

    # return res_text

def get_user_info(token):

    url = get_links()["user-info-uri"]

    headers = {
        "Authorization": "bearer " + token
    }

    res = requests.post(url, headers=headers, verify=False)

    res_text = json.loads(res.text)

    pretty_print_json(res_text)

    return res_text

# def get_roles(token):
#     response = get_user_info(token)
#
#     print("todo iscupaj roles")
#     return response["roles"]

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
    print("login")
    res = keycloak_obtain_token()
    # return

    roles = get_roles(res["access_token"])
    print(f"{roles=}")
    return
    access_token = res["access_token"]
    refresh_token = res["refresh_token"]
    # print(access_token)

    print("check valid")
    print(f"{is_valid(access_token)=}")

    print(80 * "_")

    res = get_user_info(access_token)
    print(res)

    return


    print(f"{is_valid('fake token')=}")


    print("logout")
    res = logout(refresh_token)

    print(f"{is_valid(access_token)=}")

    # res = check_validity(access_token)
    # res = check_validity("access_token")

if __name__ == '__main__':
    main()