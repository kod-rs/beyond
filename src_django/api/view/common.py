import datetime
import json

import requests
from django.http import JsonResponse

from src_django.api.tests import mocks
from src_django.settings import BEYOND_CONFIG


def false_status(response_type: str, msg: str) -> JsonResponse:
    """
    Generic JSON response if POST request fails for any reason
    Args:
        response_type: expected response type for a specific request
        msg: message describing why the request failed

    Returns:

    """
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})


def json_decode(request_body: bytes) -> dict:
    """
    JSON decode wrapper
    Args:
        request_body: body to be decoded

    Returns:
        decoded data or an empty dictionary
    """
    try:
        return json.loads(request_body)
    except Exception as e:
        print(f'Exception while decoding the body={e}')
        return {}


def datetime_from_rfc_string(rfc_string: str) -> datetime.datetime:
    """
    Convert a string in RFC 3339 format to datetime.datetime object
    Args:
        rfc_string: RFC 3339 string

    Returns:
        datetime.datetime object that contains all the data to conform to
        ISO format
    """
    dt = datetime.datetime.fromisoformat(rfc_string)
    return dt


class BeyondConnection:
    """
    Connection to Beyond platform
    """

    def __init__(self):
        self._building_by_usr_id_req_type = 'buildings_by_user_id_request'
        self._building_info_req_type = 'building_info_request'
        self._flex_demand_type = 'flexibility_demand_request'
        self._url = BEYOND_CONFIG['URL']

    def _send(self, data: dict) -> dict:
        response = requests.post(self._url, json=data)
        response_data = response.json()
        return response_data

    def req_building_by_usr_id(self, usr_id: int) -> dict:
        """
        Get all the buildings with their IDs and geolocation info for
        a specific user.
        Args:
            usr_id: user ID specific to each user

        Returns:
            object containing the requested data from Beyond platform
        """
        data = {'type': self._building_by_usr_id_req_type,
                'user_id': usr_id}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_by_usr_id()

    def req_building_info(self, building_ids):
        data = {'type': self._building_info_req_type,
                'building_ids': building_ids}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_info(None)

    def req_flex_demand(self, date):
        data = {'type': self._flex_demand_type,
                'date': date}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_get_flexibility_demand(date)
