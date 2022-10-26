import sys

import keycloak.exceptions
from keycloak import KeycloakOpenID


def keycloak_login(username: str, password: str):
    keycloak_openid = KeycloakOpenID(
        # TODO read this from somewhere
        server_url="http://localhost:8080/",
        client_id="flexopt",
        realm_name="beyond_realm",
        client_secret_key="PqwPWsOOmZw5jH3Zmvvs7zAMUDTbaZ8V")

    try:
        token = keycloak_openid.token(username=username, password=password)
        userinfo = keycloak_openid.userinfo(token['access_token'])
    except keycloak.exceptions.KeycloakAuthenticationError as e:
        return {'status': False, 'info': e.response_code}

    return {'status': True,
            'info': {'user_id': userinfo['sub'],
                     'token': token['refresh_token']}}


if __name__ == '__main__':
    resp = keycloak_login(username='mirkofleks',
                          password='mirkofleks')
    print(resp)
    sys.exit()
