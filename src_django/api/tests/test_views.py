import datetime
import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api.tests import mocks
from src_django.api.view import common


class TestLoginView(TestCase):
    def setUp(self):
        keycloak.KeycloakOpenID.token = MagicMock(
            side_effect=mocks.mock_token)
        keycloak.KeycloakOpenID.userinfo = MagicMock(
            side_effect=mocks.mock_userinfo)

    def test_login_success(self):
        client = Client()
        data = {'type': 'login_request',
                'username': 'mirkofleks',
                'password': 'mirkofleks'}

        response = client.post('/login/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'login_response'
        assert response['status'] is True
        assert isinstance(response['user_id'], str)
        assert isinstance(response['access_token'], str)
        assert isinstance(response['username'], str)
        assert isinstance(response['role'], str)
        assert response['role'] in ['AGGREGATOR', 'MANAGER']

    def test_login_fail(self):
        client = Client()
        data = {'type': 'login_request',
                'username': 'mirkofleks',
                'password': 'WRONG_PASSWORD'}

        response = client.post('/login/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'login_response'
        assert response['status'] is False
        assert response['message'] == '401'


class TestLocationView(TestCase):
    def setUp(self):
        common.BeyondConnection.req_building_by_usr_id = MagicMock(
            side_effect=mocks.mock_req_building_by_usr_id)
        common.BeyondConnection.req_building_info = MagicMock(
            side_effect=mocks.mock_req_building_info)

    def test_get_buildings_by_user_id(self):
        client = Client()
        data = {'type': 'buildings_by_user_id_request',
                'user_id': 'usr1abcdef'}

        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'buildings_by_user_id_response'
        assert len(response['buildings']) > 0
        assert isinstance(response['buildings'][0]['building_id'], str)
        assert isinstance(response['buildings'][0]['building_name'], str)
        assert isinstance(response['buildings'][0]['longitude'], float)
        assert isinstance(response['buildings'][0]['longitude'], float)

    def test_get_building_info(self):
        client = Client()

        data = {'type': 'building_info_request',
                'building_ids': mocks.ids[:3]}

        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'building_info_response'
        assert len(response['buildings_info']) != 0
        assert len(response['buildings_info'][0]['energy_info']) != 0
        timeseries = response['buildings_info'][0]['energy_info'][0]
        assert set(timeseries.keys()) == {'value', 'timestamp'}


class TestFlexibilityDemand(TestCase):
    def setUp(self):
        common.BeyondConnection.req_flex_demand = MagicMock(
            side_effect=mocks.mock_get_flexibility_demand)

    def test_flexibility_demand(self):
        client = Client()
        date = datetime.datetime(year=2022, month=4, day=10, hour=0)
        date = date.replace(tzinfo=datetime.timezone.utc).isoformat()
        data = {'type': 'flexibility_demand_request',
                'date': date}

        response = client.post('/flexibility_demand/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()
        assert response['type'] == 'flexibility_demand_response'
        assert response['status'] is True
        assert isinstance(response['demands'], list)
        assert len(response['demands']) > 0
        assert set(response['demands'][0].keys()) == {'end_time',
                                                      'flexibility',
                                                      'start_time'}


class TestAlgorithmView(TestCase):
    def test_get_buildings_by_user_id(self):
        client = Client()
        data = {'type': 'algorithm_request',
                'building_energy_list': [],
                'interval': {
                    'from': 12,
                    'to': 15},
                'flexibility_amount': 300,
                'month': None}

        building_energy_list = mocks.mock_building_energy_list()

        data['building_energy_list'] = building_energy_list
        response = client.post('/algorithm/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'algorithm_response'
        assert response['status'] is True
        assert (isinstance(response['offered_flexibility'], float)
                or isinstance(response['offered_flexibility'], int))
        assert isinstance(response['building_info'], list)
