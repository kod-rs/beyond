import datetime
import json

import requests
from django.http import JsonResponse

from src_django.api.tests import mocks
from src_django.settings import BEYOND_CONFIG


def false_status(response_type: str, msg: str) -> JsonResponse:
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})


def json_decode(request_body: bytes) -> dict:
    try:
        return json.loads(request_body)
    except Exception as e:
        print(f'Exception while decoding the body={e}')
        return {}


def datetime_from_rfc_string(rfc_string: str) -> datetime.datetime:
    dt = datetime.datetime.fromisoformat(rfc_string)
    return dt


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
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_by_usr_id()

    def req_building_info(self, req_type, building_ids):
        data = {'type': req_type,
                'building_ids': building_ids}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_info()

    def req_flex_demand(self, req_type, date):
        data = {'type': req_type,
                'date': date}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_get_flexibility_demand(None, date)
