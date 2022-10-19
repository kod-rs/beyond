import json

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import controller
from src_django.api.view import common


class PortfolioView(APIView):

    def post(self, request) -> JsonResponse:
        user_id = json.loads(request.body).get('user_id')

        if not user_id:
            return common.false_status

        portfolios = controller.portfolio.get_user_portfolios(user_id)

        if not portfolios:
            return common.false_status

        return JsonResponse({'status': True,
                             'portfolios': portfolios})
