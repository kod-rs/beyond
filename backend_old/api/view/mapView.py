from django.http import JsonResponse
from rest_framework.views import APIView

from backend_old.api.keycloak.keycloak_manager import keycloak_obtain_token


class MapView(APIView):

    def post(self, request):
        print(f"{request.user=}")
        print(f"{request.auth=}")
        print(request.data)

        username = request.data["username"]
        password = request.data["password"]
        res = keycloak_obtain_token(username, password)

        if all((i in res) for i in
               ["access_token", "expires_in", "refresh_expires_in",
                "refresh_token", "token_type", "id_token"]):
            access_token = res["access_token"]
            refresh_token = res["refresh_token"]

            response = {"ok": True,
                        "username": username,
                        "access_token": access_token,
                        "refresh_token": refresh_token}
        else:
            response = {"ok": False}

        return JsonResponse(response)
