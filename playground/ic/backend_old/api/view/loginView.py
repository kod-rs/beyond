from django.http import JsonResponse
from rest_framework.views import APIView

from playground.ic.backend_old.api.view.common import get_auth_ok_response_template


class LoginView(APIView):

    def post(self, request):
        print("login post")
        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True
        return JsonResponse(response)
