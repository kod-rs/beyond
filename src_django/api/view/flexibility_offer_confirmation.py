from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.validator.internal_api.flexibility_offer_confirmation import \
    validate_flexibility_offer_confirmation
from src_django.api.view import common


class FlexibilityOfferConfirmation(APIView):
    def __init__(self):
        super().__init__()
        self._request_type = 'flexibility_offer_confirmation_request'
        self._response_type = 'flexibility_offer_confirmation_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)

        if not validate_flexibility_offer_confirmation(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        # TODO db saving

        return JsonResponse({'type': self._response_type,
                             'status': True})
