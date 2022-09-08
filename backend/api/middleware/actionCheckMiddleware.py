from decouple import config
from backend.api.comm.comm import decode_data
from backend.api.comm.http import get_empty_response_template
from django.http import JsonResponse


class ActionCheckMiddleware:
    """check if action is present in body"""

    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        # print("ActionCheckMiddleware")

        # if "action" not in decode_data(request.body):
        #     if self.debug:
        #         print("ActionCheckMiddleware: no action in body")
        #     rejection = get_empty_response_template()
        #     return JsonResponse(rejection)

        # request.action = decode_data(request.body)["action"]

        return self.get_response(request)
