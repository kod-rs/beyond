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

        auth_credentials = {
            "access_token": None,
            "refresh_token": None,
        }

        body_content = decode_data(request.body)

        for k, v in auth_credentials.items():
            if k in body_content:
                auth_credentials[k] = body_content[k]

        res = check_tokens(
            auth_credentials["access_token"],
            auth_credentials["refresh_token"]
        )

        if not res["is_valid"]:
            rejection = get_empty_response_template()
            rejection["debug"] = "not is_validated"
            return JsonResponse(rejection)

        ip, _ = get_client_ip(request)
        auth_user(ip)

        request.access_token = res["access_token"]
        request.refresh_token = res["refresh_token"]
        request.username = res["preferred_username"]

        return self.get_response(request)
