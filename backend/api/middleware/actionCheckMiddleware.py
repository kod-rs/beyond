from backend.api.comm.role_validator import SchemeValidator
from backend.api.config.main import MIDDLEWARE_NO_ACTION
from backend.api.view.comm import check_request_contains
from decouple import config
from backend.api.comm.comm import decode_data


class ActionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"
        self.scheme_validator = SchemeValidator()

    def __call__(self, request):


        if not hasattr(request, "body"):
            print("err")

        body = getattr(request, "body")
        decoded_body = decode_data(body)
        action = decoded_body["action"]

        roles = request.roles

        request.action = decode_data(request.body)["action"]



        # request.action = check_request_contains(
        #     request=decode_data(request.body),
        #     attribute="action",
        #     raise_exception=False,
        #     default_attribute=MIDDLEWARE_NO_ACTION
        # )

        # print(f"--- {request.action}")

        return self.get_response(request)
