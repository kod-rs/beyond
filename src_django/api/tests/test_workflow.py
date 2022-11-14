import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api.tests import mocks
from src_django.api.view import common
import datetime


class WorkflowTestCase(TestCase):
    def setUp(self):
        keycloak.KeycloakOpenID.token = MagicMock(
            side_effect=mocks.mock_token)

        keycloak.KeycloakOpenID.userinfo = MagicMock(
            side_effect=mocks.mock_userinfo)

        common.BeyondConnection.req_building_by_usr_id = MagicMock(
            side_effect=mocks.mock_req_building_by_usr_id)

        common.BeyondConnection.req_building_info = MagicMock(
            side_effect=mocks.mock_req_building_info)

        common.BeyondConnection.req_flex_demand = MagicMock(
            side_effect=mocks.mock_get_flexibility_demand)

    def test_workflow(self):
        client = Client()
        data = {'type': 'login_request',
                'username': 'mirkofleks',
                'password': 'mirkofleks'}
        response = client.post('/login/',
                               json.dumps(data),
                               content_type="application/json").json()
        user_id = response['user_id']

        data = {'type': 'buildings_by_user_id_request',
                'user_id': user_id}
        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json").json()
        selected_buildings = response['buildings'][:3]
        building_ids = [b['building_id'] for b in selected_buildings]

        data = {'type': 'building_info_request',
                'building_ids': building_ids}
        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json").json()
        buildings_info = response['buildings_info']

        date = datetime.datetime(year=2022, month=4, day=10, hour=0)
        date = date.replace(tzinfo=datetime.timezone.utc).isoformat()
        data = {'type': 'flexibility_demand_request',
                'date': date}
        response = client.post('/flexibility_demand/',
                               json.dumps(data),
                               content_type="application/json").json()

        demands = response['demands']
        for d in demands:
            flex_amount = d['flexibility']

            data = {'type': 'algorithm_request',
                    'building_energy_list': buildings_info,
                    'interval': {
                        'from': d['start_time'],
                        'to': d['end_time']},
                    'flexibility_amount': flex_amount,
                    'month': None}
            response = client.post('/algorithm/',
                                   json.dumps(data),
                                   content_type="application/json")
            response = response.json()

            assert response['type'] == 'algorithm_response'
            assert response['status'] is True
            assert response['offered_flexibility'] <= flex_amount
            assert isinstance(response['building_info'], list)
            assert len(response['building_info']) > 0
            building = response['building_info'][0]
            assert building['flexibility'] <= flex_amount
            assert building['interval']['from'] == interval_from
            assert building['interval']['to'] == interval_to
