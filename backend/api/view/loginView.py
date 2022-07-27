from django.http import JsonResponse
from rest_framework.views import APIView


class LoginView(APIView):

    # used when passing args coded in url, not as args, ie pagination
    # def post(self, request, pk):
    def post(self, request):
        print("login post")

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "page": "index"
            }
        }

        return JsonResponse(response)
