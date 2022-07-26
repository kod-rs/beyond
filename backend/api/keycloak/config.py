from decouple import config


def get_urls():
    base = config("KEYCLOAK_URL")

    return {
        "authorization-uri": base + "auth",
        "user-info-uri": base + "userinfo",
        "token-uri": base + "token",
        "logout": base + "logout",
        "jwk-set-uri": base + "certs"
    }


def get_config():
    return {
        "realm": config("KEYCLOAK_REALM"),
        "client id": config("KEYCLOAK_CLIENT_ID"),
        "authorization grant type": "password",
        "client secret": config("KEYCLOAK_CLIENT_SECRET"),
        "scope": "openid profile"
    }
