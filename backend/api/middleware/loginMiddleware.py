import urllib

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
        # rejection = get_empty_response_template()
        #
        # if "HTTP_AUTHORIZATION" not in request.META:
        #     print("no authorization")
        #     return JsonResponse(rejection)

        # authorization_header = request.META['HTTP_AUTHORIZATION']

        # parsed_authorization_header = urllib.parse.unquote(authorization_header)
        # auth_type, payload = parsed_authorization_header.split(" ")

        # if auth_type != "Basic":
        #     request.is_auth = False
        #     return self.get_response(request)

        # print("user pass")
        # username, password = payload.split(":")
        # res = login(username, password)

        # if not res["is_valid"]:
        #     print("user pass err")
        #     rejection["debug"] = "user pass error"
        #     return JsonResponse(rejection)

        # todo move to auth part backend, hotfix
        ip, _ = get_client_ip(request)
        auth_user(ip)

        # fixme hardcoded for testing
        request.username = "username"
        request.access_token = 'res["access_token"]'
        request.refresh_token = 'res["refresh_token"]'
        request.is_auth = True


        # request.username = username
        # request.access_token = res["access_token"]
        # request.refresh_token = res["refresh_token"]
        # request.is_auth = True

        return self.get_response(request)
