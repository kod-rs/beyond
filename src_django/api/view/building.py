import json
import typing

import requests
from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.view import common
from src_django.settings import BEYOND_CONFIG
from src_django.api.validator import internal_api, external_api

number_type = typing.Union[int, float]


class BuildingView(APIView):
    def __init__(self):
        super().__init__()

        self._req_building_by_usr_id = 'buildings_by_user_id_request'
        self._resp_building_by_usr_id = 'buildings_by_user_id_response'

        self._req_building_info = 'building_info_request'
        self._resp_building_info = 'building_info_response'

        self._beyond = BeyondConnection()

    def post(self, request) -> JsonResponse:
        request = json.loads(request.body)
        request_type = request.get('type')

        if request_type == self._req_building_by_usr_id:
            return self._post_building_by_user_id(request)

        if request_type == self._req_building_info:
            return self._post_building_info(request)

        return common.false_status(response_type='invalid_request_response',
                                   msg='invalid request type')

    def _post_building_by_user_id(self, req: dict) -> JsonResponse:

        if not internal_api.buildings.validate_buildings_by_usr_id_req(req):
            return common.false_status(self._resp_building_by_usr_id,
                                       'invalid request')

        beyond_data = self._beyond.req_building_by_usr_id(req['type'],
                                                          req['user_id'])

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

        beyond_data = self._beyond.req_building_info(request['type'],
                                                     request['building_ids'])

        if not external_api.buildings.validate_building_info(beyond_data):
            return common.false_status(self._req_building_info,
                                       'invalid request')

        return JsonResponse({'type': self._resp_building_info,
                             'buildings_info': beyond_data['buildings_info']})


class BeyondConnection:
    def __init__(self):
        self._url = BEYOND_CONFIG['URL']

    def _send(self, data: dict) -> dict:
        response = requests.post(self._url, json=data)
        response_data = response.json()
        return response_data

    def req_building_by_usr_id(self, req_type: str, usr_id: int):
        data = {'type': req_type,
                'user_id': usr_id}
        resp = self._send(data)
        return resp

    def req_building_info(self, req_type, building_ids):
        data = {'type': req_type,
                'building_ids': building_ids}
        resp = self._send(data)
        return resp
