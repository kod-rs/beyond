from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.cqrs_c.ip import log_user_auth_attempt
from backend.api.cqrs_q.ip import check_max_count


class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        # if self.debug:
        #     print(80 * "-")
        #     print("\tIpCheckMiddleware")

        rejection = {
            "auth": {
                "status": False,
                "access-token": "",
                "refresh-token": ""
            },
            "payload": {},
            "debug": ""
        }

        ip, is_routable = get_client_ip(request)

        if is_routable:
            if self.debug:
                print(
                    "The client's IP address is publicly routable on the Internet")
        else:
            if self.debug:
                print("The client's IP address is private")

        if not ip:
            rejection["debug"] = "unable to get clients ip"
            return JsonResponse(rejection)

        if check_max_count(ip, self.max_brute_force_count):

            rejection["debug"] = "max try exceeded"
            return JsonResponse(rejection)

        log_user_auth_attempt(ip)

        request.ip = ip
        return self.get_response(request)
