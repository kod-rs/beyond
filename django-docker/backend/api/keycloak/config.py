from decouple import config


def get_urls():
    return {"authorization-uri": config("KEYCLOAK_URL") + "auth",
            "user-info-uri": config("KEYCLOAK_URL") + "userinfo",
            "token-uri": config("KEYCLOAK_URL") + "token",
            "logout": config("KEYCLOAK_URL") + "logout",
            "jwk-set-uri": config("KEYCLOAK_URL") + "certs"}


def get_config():
    return {"realm": config("KEYCLOAK_REALM"),
            "client id": config("KEYCLOAK_CLIENT_ID"),
            "authorization grant type": "password",
            "client secret": config("KEYCLOAK_CLIENT_SECRET"),
            "scope": "openid profile"}
