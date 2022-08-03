from decouple import config
from django.http import JsonResponse


class HttpsCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        if self.debug:
            print(80 * "-")
            print("\tHttpsCheckMiddleware")

        if request.is_secure() == "https":
            if self.debug:
                print("using https")
        else:
            if self.debug:
                print("using http")

            if config("HTTPS_ONLY") != "0":
                if self.debug:
                    print("rejecting")

                rejection = {
                    "auth": {
                        "status": False,
                        "access-token": "",
                        "refresh-token": ""
                    },
                    "payload": {},
                    "debug": ""
                }
                return JsonResponse(rejection)

        return self.get_response(request)
