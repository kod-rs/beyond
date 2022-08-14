from decouple import config

from backend.api.keycloak.keycloak_manager import get_roles
from backend.api.comm.role_validator import SchemeValidator
from backend.api.config.main import MIDDLEWARE_NO_ACTION, INTERNAL_SERVER_ERROR_MESSAGE


class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"
        self.scheme_validator = SchemeValidator()

    def __call__(self, request):

        access_token = request.access_token

        if not hasattr(request, "action"):
            print("internal server error, check action middleware, "
                  "he is not adding empty action")
            raise Exception(INTERNAL_SERVER_ERROR_MESSAGE)

        if request.action == MIDDLEWARE_NO_ACTION:
            print("action is empty")
            request.action_checked = MIDDLEWARE_NO_ACTION
        else:
            print(f"has action: {request.action=}")
            roles = get_roles(access_token)
            action = request.action
            r = self.scheme_validator.check_action(roles, action)
            print("checking action against role", r)
            request.action_checked = MIDDLEWARE_NO_ACTION

        request.roles = get_roles(access_token)

        return self.get_response(request)
