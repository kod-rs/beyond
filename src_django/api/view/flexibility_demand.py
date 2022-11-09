from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.validator.internal_api.algorithm import \
    validate_algorithm_request
from src_django.api.view import common


class AlgorithmView(APIView):
    def __init__(self):
        super().__init__()
        self._request_type = 'flexibility_demand_request'
        self._response_type = 'flexibility_demand_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)
        if not validate_algorithm_request(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True})
