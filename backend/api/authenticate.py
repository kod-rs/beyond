from backend.api.keycloak.keycloak_manager import keycloak_obtain_token, get_roles, get_user_info, is_valid


def login(username, password):
    res = keycloak_obtain_token(username, password)

    if all((i in res) for i in
           ["access_token", "expires_in", "refresh_expires_in", "refresh_token", "token_type", "id_token"]):
        access_token = res["access_token"]
        refresh_token = res["refresh_token"]

        responseJson = {
            "ok": True,
            "id": "user.id",
            "username": username,

            "access_token": access_token,
            "refresh_token": refresh_token
        }
    else:
        responseJson = {
            "ok": False,

        }

    return responseJson

def check_tokens(access_token, refresh_token):
    return is_valid(access_token)

    # responseJson = {
    #     "ok": is_valid(access_token),
    # }
    #
    # return responseJson

def main():
    pass

if __name__ == '__main__':
    main()