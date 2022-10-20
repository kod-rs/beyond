import json

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import controller
from src_django.api.view import common


class LocationView(APIView):

    def post(self, request) -> JsonResponse:
        portfolio_id = json.loads(request.body)
        portfolio_id = portfolio_id.get('portfolio_id')

        if not portfolio_id:
            return common.false_status

        locations = controller.location.get_for_portfolio(portfolio_id)

        return JsonResponse({'status': True,
                             'locations': list(locations)})
