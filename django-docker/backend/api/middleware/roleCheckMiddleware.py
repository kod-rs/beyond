from backend.api.keycloak.keycloak_manager import get_roles


class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.access_token
        request.roles = get_roles(access_token)
        return self.get_response(request)
