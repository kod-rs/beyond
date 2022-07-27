from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.keycloak.keycloak_manager import logout


class LogoutView(APIView):

    def post(self, request):
        print("logout post")

        print("try logout")
        logout(request.refresh_token)
        print("logout done")

        response = {
            "auth": {
                "status": True,
                "access-token": "dont need it",
                "refresh-token": "dont need it"
            },
            "payload": {
                "page": "logout",
                "msg": "byeeeee"
            }
        }

        return JsonResponse(response)
