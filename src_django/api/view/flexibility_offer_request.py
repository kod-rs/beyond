from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import controller
from src_django.api.validator.external_api.flexibility_offer_request import \
    validate_flex_offer_req_agr, validate_flex_offer_req_building
from src_django.api.view import common


class FlexibilityOfferRequest(APIView):
    """
     API for /flexibility_offer
    """

    def __init__(self):
        super().__init__()

        self._req_type_agr = 'flexibility_offer_by_aggregator'
        self._resp_type_agr = 'flexibility_offer_by_aggregator_response'

        self._req_type_building = 'flexibility_offer_by_building'
        self._resp_type_building = 'flexibility_offer_by_building_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)

        if request_body['type'] == self._req_type_agr:
            return self._post_agr(request_body)
        if request_body['type'] == self._req_type_building:
            return self._post_building(request_body)

    def _post_agr(self, request_body):
        if not validate_flex_offer_req_agr(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._resp_type_agr)

        db_data = controller.agr_flex.get_by_usr_and_time(
            user_id=request_body['user_id'],
            start_time=request_body['start_time'],
            end_time=request_body['end_time'])

        if not db_data:
            return common.false_status(msg='no data found',
                                       response_type=self._resp_type_agr)

        return JsonResponse({'type': self._resp_type_agr,
                             'status': True,
                             'user_id': request_body['user_id'],
                             'offered_flexibilities': db_data})

    def _post_building(self, request_body):
        if not validate_flex_offer_req_building(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._resp_type_building)

        db_data = controller.building_flex.get_by_building_and_time(
            building_id=request_body['building_id'],
            start_time=request_body['start_time'],
            end_time=request_body['end_time'])

        if not db_data:
            return common.false_status(msg='no data found',
                                       response_type=self._resp_type_building)

        return JsonResponse({'type': self._resp_type_building,
                             'status': True,
                             'building_id': request_body['building_id'],
                             'offered_flexibilities': db_data})
