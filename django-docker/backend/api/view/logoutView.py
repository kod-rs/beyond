from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.keycloak.keycloak_manager import logout


class LogoutView(APIView):

    def post(self, request):
        logout(request.refresh_token)
        response = {"auth": {"status": True,
                             "access-token": None,
                             "refresh-token": None},
                    "payload": {"page": "logout", }}
        return JsonResponse(response)
