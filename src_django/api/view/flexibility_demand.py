from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.validator.external_api.flexibility_demand_response import \
    validate_flexibility_demand_response
from src_django.api.validator.internal_api.flexibility_demand_request import \
    validate_flexibility_demand_request
from src_django.api.view import common


class FlexibilityDemandView(APIView):
    """
     API for /flexibility_demand
    """

    def __init__(self):
        super().__init__()
        self._request_type = 'flexibility_demand_request'
        self._response_type = 'flexibility_demand_response'

        self._beyond = common.BeyondConnection()

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)

        if not validate_flexibility_demand_request(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        beyond_data = self._beyond.req_flex_demand(request_body['date'])

        if not validate_flexibility_demand_response(beyond_data):
            return common.false_status(msg='request failed',
                                       response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True,
                             'demands': beyond_data['demands']})
