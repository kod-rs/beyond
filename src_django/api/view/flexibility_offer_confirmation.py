from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import common
from src_django.api import controller
from src_django.api.validator.internal_api.flexibility_offer_confirmation \
    import validate_flexibility_offer_confirmation


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

        if not _save(request_body):
            return common.false_status(msg='database save failed',
                                       response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True})


def _save(request_body):
    success = False
    usr_id = request_body['user_id']

    for offer in request_body['algorithm_response']['offers']:
        success = _save_total(offer, usr_id) & all(_save_buildings(offer))

    return success


def _save_total(offer, user_id):
    return controller.agr_flex.add(start_time=offer['start_time'],
                                   end_time=offer['end_time'],
                                   user_id=user_id,
                                   flexibility=offer['offered_flexibility'])


def _save_buildings(offer):
    for building in offer['building_info']:
        yield controller.building_flex.add(start_time=building['start_time'],
                                           end_time=building['end_time'],
                                           building_id=building['building_id'],
                                           flexibility=building['flexibility'])
