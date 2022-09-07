from decouple import config

from backend.api.keycloak.keycloak_manager import get_roles
from backend.api.config.main import MIDDLEWARE_NO_ACTION, INTERNAL_SERVER_ERROR_MESSAGE
from backend.api.startup import startup_configuration
from backend.api.role_action_validation.new_role_validation import check

class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"
        # self.scheme_validator = SchemeValidator()

    def __call__(self, request):
        print("RoleCheckMiddleware")

        access_token = request.access_token

        # if not hasattr(request, "action"):
        #     print("internal server error, check action middleware, "
        #           "he is not adding empty action")
        #     raise Exception(INTERNAL_SERVER_ERROR_MESSAGE)
        #
        # if request.action == MIDDLEWARE_NO_ACTION:
        #     print("action is empty")
        #     request.action_checked = MIDDLEWARE_NO_ACTION
        # else:
        roles = get_roles(access_token)
        # print(f"{roles=}")
        request.roles = roles
        # print(request.META)
        # print(80 * "-")
        print()
        # print(request.method, type(request.method))
        # print(request.path, type(request.method))

        t = check(role=roles,
                  path=request.path,
                  method=request.method
                  )
        print(t)

        # if (hasattr(request.META, "REQUEST_METHOD")):
        #     print(80 * "-")
        #     print(getattr(request.META, "REQUEST_METHOD"))
        # print("get locations", request.META.REQUEST_METHOD)

        # print(request.META)

        roles = request.roles
        print(f"{roles=}")

        # action = request.action
            # print(f"{roles=} {action=} {request}")

            #     # print(request.META)
            #
            #     if hasattr(request, "POST"):
            #         print(request.POST)
            #         print("post")
            #         username = request.POST.get('REQUEST_METHOD', default='xxx')
            #         print(f"{username=}")
            #         if hasattr(request.POST, "REQUEST_METHOD"):
            #             method = request.POST.REQUEST_METHOD
            #             print("method", method)
            #         else:
            #             print("nema")
            #
            #     elif hasattr(request, "GET"):
            #         print("get")
            #     else:
            #         print("else")
            #
            #     if hasattr(request.META, "REQUEST_METHOD"):
            #         method = request.META.REQUEST_METHOD
            #         print("method", method)
            #     else:
            #         print("nema")

            # method = request.META.get("REQUEST_METHOD", default=None)
            # path = request.META.get("PATH_INFO", default=None)
            # print(f"{method=} {path=}")

            # startup_configuration.get_scheme_validator().check_action(roles, action)
            # request.action_checked = MIDDLEWARE_NO_ACTION

        # request.roles = get_roles(access_token)

        return self.get_response(request)
