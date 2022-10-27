import json
import typing

import requests
from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.view import common
from src_django.settings import BEYOND_CONFIG


class BuildingView(APIView):
    def __init__(self):
        super().__init__()
        self._request_type = 'buildings_by_user_id_request'
        self._response_type = 'buildings_by_user_id_response'

    def post(self, request) -> JsonResponse:
        request = json.loads(request.body)

        request_type = request.get('type')
        user_id = request.get('user_id')

        if request_type != self._request_type or not user_id:
            return common.false_status(self._response_type, 'invalid request')

        beyond_data = _beyond_request(request_type, user_id)

        if not _validate(beyond_data):
            return common.false_status(self._response_type, 'request failed')

        return JsonResponse({'type': self._response_type,
                             'buildings': beyond_data.get('buildings')})


number_type = typing.Union[int, float]


def _validate(data):
    if data.get('type') != 'buildings_by_user_id_request':
        return False
    if not data.get('buildings') or not isinstance(data['buildings'], list):
        return False
    for building in data['buildings']:
        if not isinstance(building.get('building_id'), str):
            return False
        if not isinstance(building.get('building_name'), str):
            return False
        if not isinstance(building.get('latitude'), number_type):
            return False
        if not isinstance(building.get('longitude'), number_type):
            return False
    return True


def _beyond_request(request_type, user_id):
    data = {'type': request_type,
            'user_id': user_id}
    response = requests.post(BEYOND_CONFIG['URL'], json=data)
    response_data = response.json()
    return response_data
