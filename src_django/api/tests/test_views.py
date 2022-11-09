import datetime
import json
import random
from pathlib import Path
from unittest.mock import MagicMock

import keycloak
import pandas as pd
from django.test import Client
from django.test import TestCase

from src_django.api.view import common


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
            return_value={'sub': '5u8',
                          'realm_access': {'roles': ['AGGREGATOR']},
                          'preferred_username': 'mirkofleks'})

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
        def req_building_by_usr_id_mock(*_):
            buildings = []
            for i in range(100):
                buildings.append({
                    'building_id': f'b_{i}',
                    'building_name': f'building_name_{i}',
                    'address': f'Ilica {i}',
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

        common.BeyondConnection.req_building_by_usr_id = MagicMock(
            side_effect=req_building_by_usr_id_mock)

        common.BeyondConnection.req_building_info = MagicMock(
            side_effect=req_building_info_mock)

    def test_get_buildings_by_user_id(self):
        client = Client()
        data = {'type': 'buildings_by_user_id_request',
                'user_id': 'usr1abcdef'}

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
        assert len(response['buildings_info']) != 0
        assert len(response['buildings_info'][0]['info']) != 0
        timeseries = response['buildings_info'][0]['info'][0]
        assert set(timeseries.keys()) == {'value', 'timestamp'}


def _get_building_energy_list():
    ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
           'ZIV0034703915', 'ZIV0034704013',
           'ZIV0034703953', 'ZIV0034703954')
    df = pd.read_csv(Path(__file__).parent.resolve() / 'active im en.csv')
    rows = [df.iloc[index] for index in range(len(df))]
    building_energy_list = []
    for b_id in ids[:3]:
        timeseries = []
        for row in rows:
            ts = datetime.datetime.strptime(row['Timestamp'][:-4],
                                            "%Y-%m-%d %H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc).isoformat()
            timeseries.append({'timestamp': ts,
                               'value': row[b_id]})
        building_energy_list.append({'building_id': b_id,
                                     'energy_info': timeseries})
    return building_energy_list


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

        building_energy_list = _get_building_energy_list()

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


class TestFlexibilityDemand(TestCase):
    def setUp(self):
        def _get_flexibility_demand_mock(_, date):
            date = common.datetime_from_rfc_string(date)
            demands = []
            for i in range(3):
                demands.append({
                    'start_time': date.replace(hour=13 + i).isoformat(),
                    'end_time': date.replace(hour=13 + 1 + i).isoformat(),
                    'flexibility': random.uniform(100, 200)})
            return {'type': 'flexibility_demand_response',
                    'demands': demands}

        common.BeyondConnection.req_flex_demand = MagicMock(
            side_effect=_get_flexibility_demand_mock)

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
