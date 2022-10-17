from decouple import config
from backend_old.api.comm.comm import get_empty_response_template
from django.http import JsonResponse

class BodyCheckMiddleware:
    """check if has body"""

    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print("BodyCheckMiddleware")

        if not hasattr(request, "body"):
            if self.debug:
                print("BodyCheckMiddleware: no body")
            rejection = get_empty_response_template()
            return JsonResponse(rejection)

        return self.get_response(request)
