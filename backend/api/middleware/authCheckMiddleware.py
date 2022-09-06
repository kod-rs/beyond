import urllib

from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.authenticate import login, check_tokens
from backend.api.comm.comm import decode_data
from backend.api.cqrs_c.ip import auth_user
from backend.api.comm.http import get_empty_response_template


class AuthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print("AuthCheckMiddleware")

        if request.is_auth:
            return self.get_response(request)

        authorization_header = request.META['HTTP_AUTHORIZATION']
        parsed_authorization_header = urllib.parse.unquote(authorization_header)
        auth_type, payload = parsed_authorization_header.split(" ")

        if auth_type == "Digest":
            # todo https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
            print("Digest")

            access_token, refresh_token = payload.split(":")
            # print(payload)
            res = check_tokens(
                access_token,
                refresh_token
            )

        else:
            res = {"is_valid": False}

        if not res["is_valid"]:
            print("not valid")
            rejection = get_empty_response_template()
            rejection["debug"] = "not is_validated"
            return JsonResponse(rejection)

        ip, _ = get_client_ip(request)
        auth_user(ip)

        request.access_token = res["access_token"]
        request.refresh_token = res["refresh_token"]
        request.username = res["preferred_username"]

        return self.get_response(request)
