from django.http import JsonResponse
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request):
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token},
                    "payload": {"page": "index"}}
        return JsonResponse(response)
