from django.http import JsonResponse
from rest_framework.views import APIView

from backend.api.view.common import get_auth_ok_response_template


class IndexView(APIView):

    def get(self, request):
        response = get_auth_ok_response_template(request)
        response["payload"]["status"] = True

        return JsonResponse(response)
