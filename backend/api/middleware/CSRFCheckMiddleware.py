from decouple import config
from django.http import JsonResponse
from ipware import get_client_ip

from backend.api.cqrs_c.ip import log_user_auth_attempt
from backend.api.cqrs_q.ip import check_max_count
from backend.api.cqrs_q.csrf import get_by_ip
from backend.api.comm.comm import decode_data

class CSRFCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        if self.debug:
            print(80 * "-")
            print("\tCSRFCheckMiddleware")

        # ovo cupamo iz baze

        ip = request.ip
        # print(f"{ip=}")

        pl = get_by_ip(ip)

        # print(f"{pl=}")
        # print(pl.synchronizer_token)
        # print(pl.encrypted_token)
        # print(pl.double_submitted_cookie)

        # ovo je stvarno stanje situacije
        auth_credentials = {
            "synchronizer_token": None,
            "synchronizer-token": None,

            # todo
            # "encrypted_token": None,
            # "encrypted-token": None,
            # "double_submitted_cookie": None,
            # "double-submitted-cookie": None
        }

        if request.headers:

            for k, v in auth_credentials.items():
                if k in request.headers:
                    auth_credentials[k] = request.headers[k]

        if request.body:
            body_content = decode_data(request.body)

            for k, v in auth_credentials.items():
                if k in body_content:
                    auth_credentials[k] = body_content[k]

        # for k, v in auth_credentials.items():
        #     print(k, v)

        # print("expected", pl.synchronizer_token)
        # print("got     ", auth_credentials["synchronizer_token"])

        # todo refactor when impl other
        if (auth_credentials["synchronizer_token"] == pl.synchronizer_token) or (auth_credentials["synchronizer-token"] == pl.synchronizer_token):
            print("match for synchronizer_token_match")
            request.synchronizer_token_match = True
        else:
            print("no match for synchronizer_token_match")
            request.synchronizer_token_match = False

        # if any(i == pl.synchronizer_token for i in auth_credentials):
        #     print("match")



        # if pl["synchronizer_token"]:
        #     print(pl["synchronizer_token"])
        # if pl.encrypted_token:
        #     print(f"{pl.encrypted_token=}")
        # if pl.double_submitted_cookie:
        #     print(f"{pl.double_submitted_cookie=}")

        # rejection = {
        #     "auth": {
        #         "status": False,
        #         "access-token": "",
        #         "refresh-token": ""
        #     },
        #     "payload": {},
        #     "debug": ""
        # }
        #
        # ip, is_routable = get_client_ip(request)
        #
        # if is_routable:
        #     if self.debug:
        #         print(
        #             "The client's IP address is publicly routable on the Internet")
        # else:
        #     if self.debug:
        #         print("The client's IP address is private")
        #
        # if not ip:
        #     if self.debug:
        #         print("unable to get clients ip")
        #     rejection["debug"] = "unable to get clients ip"
        #     return JsonResponse(rejection)
        #
        # if check_max_count(ip, self.max_brute_force_count):
        #     if self.debug:
        #         print("max try exceeded")
        #     rejection["debug"] = "max try exceeded"
        #     return JsonResponse(rejection)
        #
        # log_user_auth_attempt(ip)
        #
        # if self.debug:
        #     print("returning")
        #
        # request.ip = ip
        return self.get_response(request)
