from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.cqrs_c.ip import log_user_auth_attempt
from backend.api.cqrs_q.ip import check_max_count


class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_brute_force_count = int(config("MAX_BRUTE_ATTEMPTS"))

    def __call__(self, request):
        rejection = {"auth": {"status": False,
                              "access-token": "",
                              "refresh-token": ""},
                     "payload": {},
                     "debug": ""}

        ip, _ = get_client_ip(request)

        if not ip:
            rejection["debug"] = "unable to get clients ip"
            return JsonResponse(rejection)

        if check_max_count(ip, self.max_brute_force_count):
            rejection["debug"] = "max try exceeded"
            return JsonResponse(rejection)

        log_user_auth_attempt(ip)
        request.ip = ip
        return self.get_response(request)
