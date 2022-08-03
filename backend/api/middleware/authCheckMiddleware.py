from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.authenticate import login, check_tokens
from backend.api.comm.comm import decode_data
from backend.api.cqrs_c.ip import auth_user


class AuthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print(80 * "-")

        rejection = {
            "auth": {
                "status": False,
                "access-token": "",
                "refresh-token": ""
            },
            "payload": {},
            "debug": ""
        }

        auth_credentials = {
            "username": None,
            "password": None,
            "access_token": None,
            "refresh_token": None,
            "access-token": None,
            "refresh-token": None
        }

        if request.headers:

            for k, v in auth_credentials.items():
                if k in request.headers:
                    auth_credentials[k] = request.headers[k]

        if request.body:
            print("decoding", request.body)
            body_content = decode_data(request.body)

            for k, v in auth_credentials.items():
                if k in body_content:
                    auth_credentials[k] = body_content[k]

        for i in auth_credentials.items():
            print(i)

        username = auth_credentials["username"]
        password = auth_credentials["password"]
        access_token = auth_credentials["access_token"] if auth_credentials[
            "access_token"] else auth_credentials["access-token"]
        refresh_token = auth_credentials["refresh_token"] if auth_credentials[
            "refresh_token"] else auth_credentials["refresh-token"]

        action = None
        if request.headers:
            if "action" in request.headers:
                action = request.headers["action"]

        if request.body:
            print("decoding", request.body)
            body_content = decode_data(request.body)
            if "action" in body_content:
                action = body_content["action"]

        if self.debug:
            print(f"{username=}")
            print(f"{password=}")
            print(f"{str(access_token)[:15]=}")
            print(f"{str(refresh_token)[:15]=}")

        is_validated = None

        if username and password:
            if self.debug:
                print("using user pass")

            res = login(username, password)

            is_validated = res["ok"]

        elif access_token and refresh_token:

            if self.debug:
                print("using tokens")

            res = check_tokens(
                access_token,
                refresh_token
            )

            is_validated = res["is_valid"]

        if not is_validated:
            if self.debug:
                print("not valid")

            rejection["debug"] = "not is_validated"
            return JsonResponse(rejection)

        if self.debug:
            print("returning correct")

        access_token = res["access_token"]
        refresh_token = res["refresh_token"]

        ip, _ = get_client_ip(request)
        auth_user(ip)

        request.action = action
        request.access_token = access_token
        request.refresh_token = refresh_token

        if self.debug:
            print("returning")

        return self.get_response(request)
