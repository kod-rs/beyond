from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.authenticate import login, check_tokens
from backend.api.cqrs_c.ip import log_user_auth_attempt, auth_user
from backend.api.cqrs_q.ip import check_max_count


class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))

    def __call__(self, request):

        print(80 * "-")
        print("ip & https check")

        if request.is_secure() == "https":
            print("using https")
        else:
            print("todo using http")

        ip, is_routable = get_client_ip(request)

        if is_routable:
            print(
                "The client's IP address is publicly routable on the Internet")
        else:
            print("The client's IP address is private")

        rejection = {
            "rejected": True
        }

        if not ip:
            print("unable to get clients ip")

            return JsonResponse(rejection)

        if check_max_count(ip, self.max_brute_force_count):
            print("max try exceeded")
            return JsonResponse(rejection)

        log_user_auth_attempt(ip)

        is_validated = None
        if request.headers:

            if all((i in request.headers) for i in ["username", "password"]):
                print("using user pass")

                is_validated = login(
                    request.headers["username"],
                    request.headers["password"]
                )["ok"]

            elif all((i in request.headers) for i in
                     ["access-token", "refresh-token"]):
                print("using tokens")

                is_validated = check_tokens(
                    request.headers["access-token"],
                    request.headers["refresh-token"]
                )["is_valid"]

        if not is_validated:
            return JsonResponse(rejection)

        else:
            auth_user(ip)
            return self.get_response(request)
