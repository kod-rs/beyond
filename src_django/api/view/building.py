import typing

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.validator import internal_api, external_api
from src_django.api.view import common

number_type = typing.Union[int, float]


class BuildingView(APIView):
    """
     API for /buildings
     """

    def __init__(self):
        super().__init__()

        self._req_building_by_usr_id = 'buildings_by_user_id_request'
        self._resp_building_by_usr_id = 'buildings_by_user_id_response'

        self._req_building_info = 'building_info_request'
        self._resp_building_info = 'building_info_response'

        self._beyond = common.BeyondConnection()

    def post(self, request) -> JsonResponse:
        request = common.json_decode(request.body)
        request_type = request.get('type')

        if request_type == self._req_building_by_usr_id:
            return self._post_building_by_user_id(request)

        if request_type == self._req_building_info:
            return self._post_building_info(request)

    def _post_building_by_user_id(self, req: dict) -> JsonResponse:
        if not internal_api.buildings.validate_buildings_by_usr_id_req(req):
            return common.false_status(self._resp_building_by_usr_id,
                                       'invalid request')
        beyond_data = self._beyond.req_building_by_usr_id(req['user_id'])

        if not external_api.buildings.validate_buildings_by_usr_id_resp(
                beyond_data):
            return common.false_status(self._resp_building_by_usr_id,
                                       'request failed')

        return JsonResponse({'type': self._resp_building_by_usr_id,
                             'buildings': beyond_data.get('buildings')})

    def _post_building_info(self, request: dict) -> JsonResponse:
        if not internal_api.buildings.validate_building_info_req(request):
            return common.false_status(self._req_building_info,
                                       'invalid request')

        beyond_data = self._beyond.req_building_info(request['building_ids'])

        if not external_api.buildings.validate_building_info(beyond_data):
            return common.false_status(self._req_building_info,
                                       'invalid request')

        return JsonResponse({'type': self._resp_building_info,
                             'buildings_info': beyond_data['buildings_info']})
