from django.http import JsonResponse
from ipware import get_client_ip
from backend.api.cqrs_c.ip import log_user_auth_attempt, auth_user
from backend.api.cqrs_q.ip import check_max_count
from backend.api.authenticate import login, check_tokens


class IpCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.max_brute_force_count = 500

    def check_username_password(self, username, password):
        print("username password")

        return login(username, password)["ok"]

    def check_tokens(self, access_token, refresh_token):
        """"""
        return check_tokens(access_token, refresh_token)["is_valid"]

    def __call__(self, request):

        print(80 * "-")
        print("ip & https check")

        if request.is_secure() == "https":
            print("using https")
        else:
            print("todo using http")

        # print(request.headers)
        ip, is_routable = get_client_ip(request)

        if is_routable:
            print("The client's IP address is publicly routable on the Internet")
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
        print("ipc 1")
        if request.headers:

            if all((i in request.headers) for i in ["username", "password"]):
                print("ipc 2")

                is_validated = self.check_username_password(
                    request.headers["username"],
                    request.headers["password"]
                )

            elif all((i in request.headers) for i in
                     ["access-token", "refresh-token"]):
                print("using tokens")
                print("ipc 3")

                is_validated = self.check_tokens(
                    request.headers["access_token"],
                    request.headers["refresh_token"]
                )
            print("ipc 4")


        if not is_validated:
            return JsonResponse(rejection)

        else:
            auth_user(ip)
            return self.get_response(request)
