from django.http import JsonResponse
from rest_framework.views import APIView


class UserInfoView(APIView):
    def get(self, request):
        response = {"auth": {"status": True,
                             "access-token": request.access_token,
                             "refresh-token": request.refresh_token},
                    "payload": {"status": True,
                                "role": request.role}}
        return JsonResponse(response)
