from decouple import config
from django.http import JsonResponse


class HttpsCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.is_secure() == "https":
            pass  # TODO
        else:
            if config("HTTPS_ONLY") != "0":
                rejection = {"auth": {"status": False,
                                      "access-token": "",
                                      "refresh-token": ""},
                             "payload": {},
                             "debug": ""}
                return JsonResponse(rejection)
        return self.get_response(request)
