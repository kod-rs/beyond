import json

from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.authenticate import login, check_tokens
from backend.api.cqrs_c.ip import log_user_auth_attempt, auth_user
from backend.api.cqrs_q.ip import check_max_count
from backend.api.comm.comm import decode_data
from backend.api.keycloak.keycloak_manager import get_roles

class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        rejection = {
            "auth": {
                "status": False,
                "access-token": "",
                "refresh-token": ""
            },
            "payload": {},
            "debug": ""
        }

        print(80 * "-")

        print("todo check role")

        if self.debug:
            print("ip & https check")


        if request.is_secure() == "https":
            if self.debug:
                print("using https")
        else:
            if self.debug:
                print("using http")

            if config("HTTPS_ONLY") != 0:
                return JsonResponse(rejection)

        ip, is_routable = get_client_ip(request)

        if is_routable:
            if self.debug:
                print(
                    "The client's IP address is publicly routable on the Internet")
        else:
            if self.debug:
                print("The client's IP address is private")


        if not ip:
            if self.debug:
                print("unable to get clients ip")
            rejection["debug"] = "unable to get clients ip"
            return JsonResponse(rejection)

        if check_max_count(ip, self.max_brute_force_count):
            if self.debug:
                print("max try exceeded")
            rejection["debug"] = "max try exceeded"
            return JsonResponse(rejection)

        log_user_auth_attempt(ip)

        username = None
        password = None
        access_token = None
        refresh_token = None

        if request.headers:
            if all((i in request.headers) for i in ["username", "password"]):
                username=request.headers["username"]
                password=request.headers["password"]

            if all((i in request.headers) for i in
                     ["access-token", "refresh-token"]):

                access_token = request.headers["access-token"]
                refresh_token = request.headers["refresh-token"]

        if request.body:
            print("decoding", request.body)
            body_content = decode_data(request.body)

            if all((i in body_content) for i in ["username", "password"]):
                username = body_content["username"]
                password = body_content["password"]

            if all((i in body_content) for i in
                   ["access-token", "refresh-token"]):
                access_token = body_content["access-token"]
                refresh_token = body_content["refresh-token"]

            if all((i in body_content) for i in
                     ["access_token", "refresh_token"]):

                access_token = body_content["access_token"]
                refresh_token = body_content["refresh_token"]

        if self.debug:
            print(f"{username=}")
            print(f"{password=}")
            print(f"{str(access_token)[:15]=}")
            print(f"{str(refresh_token)[:15]=}")


        is_validated = None
        # if request.headers:

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
            rejection["debug"] = "not is_validated"
            return JsonResponse(rejection)

        else:
            # todo
            access_token = res["access_token"]
            refresh_token = res["refresh_token"]



            auth_user(ip)
            request.roles = get_roles(access_token)
            request.access_token = access_token
            request.refresh_token = refresh_token
            return self.get_response(request)
