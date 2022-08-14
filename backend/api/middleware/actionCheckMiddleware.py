from decouple import config

from backend.api.keycloak.keycloak_manager import get_roles
from backend.api.comm.role_validator import SchemeValidator
from backend.api.config.main import MIDDLEWARE_NO_ACTION

class ActionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"
        self.scheme_validator = SchemeValidator()

    def __call__(self, request):
        if hasattr(request, "action"):
            # if request.action:
            #     print("action is not none")
            if not request.action:
                # print("action is none")
                request.action = MIDDLEWARE_NO_ACTION
            # pass
            # print(f"has action: {request.action=}")
        else:
            # print("no action, adding no action")
            request.action = MIDDLEWARE_NO_ACTION

        return self.get_response(request)
