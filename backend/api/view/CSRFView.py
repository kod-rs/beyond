from django.http import JsonResponse
from rest_framework.views import APIView
from backend.api.csrf.main import get_synchronizer_token
from backend.api.cqrs_c.csrf import create

class CSRFView(APIView):

    def post(self, request):
        print("csrf post")

        synchronizer_token = get_synchronizer_token()
        create(
            ip=request.ip,
            synchronizer_token=synchronizer_token,
            encrypted_token=None,
            double_submitted_cookie=None
        )


        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "synchronizer_token": synchronizer_token
            }
        }

        return JsonResponse(response)
