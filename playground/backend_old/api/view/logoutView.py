from django.http import JsonResponse
from rest_framework.views import APIView

from playground.backend_old.api.keycloak.keycloak_manager import logout
from playground.backend_old.api.view.common import get_auth_ok_response_template


class LogoutView(APIView):

    def post(self, request):
        print("logout post")
        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = logout(request.refresh_token)
        return JsonResponse(response)
