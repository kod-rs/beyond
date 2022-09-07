from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.cqrs_c.csrf import create
from backend.api.csrf.main import get_synchronizer_token
from backend.api.view.comm import get_auth_ok_response_template


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

        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True
        response["payload"]["synchronizer_token"] = synchronizer_token

        return JsonResponse(response)
