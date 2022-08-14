from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.authenticate import login, check_tokens
from backend.api.comm.comm import decode_data
from backend.api.cqrs_c.ip import auth_user
from backend.api.comm.http import get_empty_response_template


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print("LoginMiddleware")

        auth_credentials = {
            "username": None,
            "password": None,
        }

        body_content = decode_data(request.body)

        for k, v in auth_credentials.items():
            if k in body_content:
                auth_credentials[k] = body_content[k]

        if not all(auth_credentials.values()):
            request.is_auth = False
            return self.get_response(request)

        res = login(
            auth_credentials["username"],
            auth_credentials["password"]
        )

        if not res["ok"]:
            rejection = get_empty_response_template()
            rejection["debug"] = "not is_validated"
            return JsonResponse(rejection)

        ip, _ = get_client_ip(request)
        auth_user(ip)

        request.username = auth_credentials["username"]
        request.access_token = res["access_token"]
        request.refresh_token = res["refresh_token"]
        request.is_auth = True

        return self.get_response(request)
