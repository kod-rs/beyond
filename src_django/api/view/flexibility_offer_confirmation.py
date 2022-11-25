from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import controller
from src_django.api.validator.internal_api.flexibility_offer_confirmation \
    import validate_flexibility_offer_confirmation
from api import common


class FlexibilityOfferConfirmation(APIView):
    """
     API for /flexibility_offer_confirmation
    """

    def __init__(self):
        super().__init__()
        self._request_type = 'flexibility_offer_confirmation_request'
        self._response_type = 'flexibility_offer_confirmation_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)

        if not validate_flexibility_offer_confirmation(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        start = request_body['algorithm_response']['interval']['from']
        end = request_body['algorithm_response']['interval']['to']
        flex = request_body['algorithm_response']['offered_flexibility']

        success = controller.agr_flex.add(
            start_time=start,
            end_time=end,
            user_id=request_body['user_id'],
            flexibility=flex)

        for building in request_body['algorithm_response']['building_info']:
            success &= controller.building_flex.add(
                start_time=building['interval']['from'],
                end_time=building['interval']['to'],
                building_id=building['building_id'],
                flexibility=building['flexibility'])

        if not success:
            return common.false_status(msg='database save failed',
                                       response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True})
