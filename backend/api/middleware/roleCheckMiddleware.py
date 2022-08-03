from decouple import config

from backend.api.keycloak.keycloak_manager import get_roles


class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print(80 * "-")
        print("role check")

        access_token = request.access_token
        print(access_token)

        request.roles = get_roles(access_token)
        print(request.roles)

        if self.debug:
            print("returning")

        return self.get_response(request)
