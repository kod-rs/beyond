from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.view.comm import get_auth_ok_response_template


class LoginView(APIView):

    # used when passing args coded in url, not as args, ie pagination
    # def post(self, request, pk):
    def post(self, request):
        print("login post")

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True

        return JsonResponse(response)
