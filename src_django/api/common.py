import datetime
import json
from pathlib import Path

import requests
from dateutil import parser
from django.http import JsonResponse

from src_django.api import cryptography_wrapper
from src_django.api.tests import mocks
from src_django.settings import BEYOND_CONFIG

internal_requests_mapping = {
    'login_request': 'login_response',
    'algorithm_request': 'algorithm_response',
    'buildings_by_user_id_request': 'buildings_by_user_id_response',
    'building_info_request': 'building_info_response',
    'flexibility_demand_request': 'flexibility_demand_response',
    'flexibility_offer_confirmation_request': (
        'flexibility_offer_confirmation_response')}

beyond_requests_mapping = {
    'flexibility_offer_by_aggregator': (
        'flexibility_offer_by_aggregator_response'),
    'flexibility_offer_by_building': 'flexibility_offer_by_building_response'}

token_types = {
    'algorithm_request',
    'buildings_by_user_id_request',
    'building_info_request',
    'flexibility_demand_request',
    'flexibility_offer_confirmation_request'
}


def false_status(response_type: str, msg: str) -> JsonResponse:
    """
    Generic JSON response if POST request fails for any reason

    Args:
        response_type: expected response type for a specific request
        msg: message describing why the request failed

    Returns:
        A false status JsonResponse message with the type being set to
        response_type, status set to False, and the message being set to msg

    """
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})


def json_decode(request_body: bytes) -> dict:
    """
    JSON decode wrapper

    Args:
        request_body: message to be decoded

    Returns:
        Decoded data or an empty dictionary
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
    dt = parser.parse(rfc_string)
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
        private_key_path = BEYOND_CONFIG['FLEXOPT_PRIVATE_KEY_PATH']
        private_key_path = Path(private_key_path)
        private_key_bytes = cryptography_wrapper.load_private_key(
            private_key_path)
        private_key = cryptography_wrapper.get_private_key_from_bytes(
            private_key_bytes)
        self._flexopt_private_key = private_key

    def _send(self, data: dict) -> dict:
        signature = cryptography_wrapper.sign(self._flexopt_private_key, data)
        data = {**data, 'signature': signature}
        response = requests.post(self._url, json=data)
        response_data = response.json()
        return response_data

    def req_building_by_usr_id(self, usr_id: int) -> dict:
        """
        Get all the buildings with their IDs and geolocation info for
        a specific user from the Beyond platform.
        Args:
            usr_id: user ID specific to each user

        Returns:
            Object containing the requested data from Beyond platform
            as specified in the
            'external_api/building_info_response.yaml' schema
        """
        data = {'type': self._building_by_usr_id_req_type,
                'user_id': usr_id}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_by_usr_id(usr_id)

    def req_building_info(self, building_ids: list) -> dict:
        """
        Get all the building information (name, id, geolocation, address)
        for all the buildings represented by their building ids

        Args:
            building_ids: Array of building ids

        Returns:
            Building information as specified by the
            'external_api/buildings_by_user_id_response.yaml' schema
        """
        data = {'type': self._building_info_req_type,
                'building_ids': building_ids}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_req_building_info(building_ids)

    def req_flex_demand(self, date: str):
        """
        Get the flexibility demands for the requested date from the Beyond
        platform.

        Args:
            date: RFC 3339 string

        Returns:
            Flexibility demand(s) as specified by the
            'external_api/flexibility_demand_response.yaml' schema
        """
        data = {'type': self._flex_demand_type,
                'date': date}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return mocks.mock_get_flexibility_demand(date)
