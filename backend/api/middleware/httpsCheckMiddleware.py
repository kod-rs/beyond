from decouple import config
from django.http import JsonResponse
from backend.api.middleware.comm import DebuggableMiddleware
from backend.api.middleware.comm import get_empty_response_template

class HttpsCheckMiddleware(DebuggableMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)

    def __call__(self, request):
        print()

        if request.is_secure() == "https":
            return self.get_response(request)

        if config("HTTPS_ONLY") != "0":

            rejection = get_empty_response_template()
            return JsonResponse(rejection)

        return self.get_response(request)
