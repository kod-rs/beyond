import datetime
import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api.view import building


class TestLoginView(TestCase):
    def setUp(self):
        def mock_token(username, password):
            if username == password == 'mirkofleks':
                return {'refresh_token': 'r3f75h',
                        'access_token': 'ac355_70k3n'}
            else:
                raise keycloak.exceptions.KeycloakAuthenticationError(
                    response_code=401)

        keycloak.KeycloakOpenID.token = MagicMock(
            side_effect=mock_token)
        keycloak.KeycloakOpenID.userinfo = MagicMock(
            return_value={'sub': '5u8'})

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
        def req_building_by_usr_id_mock(*_):
            buildings = []
            for i in range(100):
                buildings.append({
                    'building_id': f'b_{i}',
                    'building_name': f'building_name_{i}',
                    'latitude': i + 0.3,
                    'longitude': i + 0.4})
            return {'type': 'buildings_by_user_id_response',
                    'buildings': buildings}

        def req_building_info_mock(*_):
            timeseries = []
            dt = datetime.datetime.now(datetime.timezone.utc)
            for i in range(2):
                dt += datetime.timedelta(minutes=i + 1)
                timeseries.append({'value': i + 100,
                                   'timestamp': dt.isoformat()})
            buildings_info = []
            for i in range(2):
                buildings_info.append({'building_id': f'b{i + 1}',
                                       'info': timeseries})
            return {'type': 'building_info_response',
                    'buildings_info': buildings_info}

        building.BeyondConnection.req_building_by_usr_id = MagicMock(
            side_effect=req_building_by_usr_id_mock)

        building.BeyondConnection.req_building_info = MagicMock(
            side_effect=req_building_info_mock)

    def test_get_buildings_by_user_id(self):
        client = Client()
        data = {'type': 'buildings_by_user_id_request',
                'user_id': 1}

        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'buildings_by_user_id_response'
        assert len(response['buildings']) == 100
        assert isinstance(response['buildings'][0]['building_id'], str)
        assert isinstance(response['buildings'][0]['building_name'], str)
        assert isinstance(response['buildings'][0]['longitude'], float)
        assert isinstance(response['buildings'][0]['longitude'], float)

    def test_get_building_info(self):
        client = Client()
        data = {'type': 'building_info_request',
                'building_ids': ['b1', 'b2', 'b3']}

        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'building_info_response'
        assert len(response['buildings_info']) == 2
        assert len(response['buildings_info'][0]['info']) == 2
        timeseries = response['buildings_info'][0]['info'][0]
        assert set(timeseries.keys()) == {'value', 'timestamp'}