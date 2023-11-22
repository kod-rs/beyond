import datetime
import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api import common
from src_django.api import cryptography_wrapper
from src_django.api.models import UserSession
from src_django.api.tests import mocks


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

        # login through Keycloak
        data = {'type': 'login_request',
                'username': 'urbener_acc',
                'password': 'urbener'}
        response = client.post('/login/',
                               json.dumps(data),
                               content_type="application/json").json()
        user_id = response['user_id']

        access_token = UserSession.objects.get().user_token
        # get building ids, names and coordinates - automatically from Beyond
        data = {'type': 'buildings_by_user_id_request',
                'user_id': user_id,
                'access_token': access_token}
        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json").json()

        # get consumption info for 'selected' buildings from Beyond
        selected_buildings = response['buildings'][:3]
        data = {'type': 'building_info_request',
                'building_ids': [b['building_id'] for b in selected_buildings],
                'access_token': access_token}
        response = client.post('/buildings/',
                               json.dumps(data),
                               content_type="application/json").json()

        # get flexibility demands for a selected data from Beyond
        buildings_info = response['buildings_info']
        date = datetime.datetime(year=2023, month=3, day=10, hour=0)
        date = date.replace(tzinfo=datetime.timezone.utc).isoformat()
        data = {'type': 'flexibility_demand_request',
                'date': date,
                'access_token': access_token}
        response = client.post('/flexibility_demand/',
                               json.dumps(data),
                               content_type="application/json").json()

        # calculate flexibilities for all the demands
        data = {'type': 'algorithm_request',
                'building_energy_list': buildings_info,
                'flexibility_demands': response['demands'],
                'access_token': access_token}

        response = client.post('/algorithm/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        # for later use
        first_offer = response['offers'][0]
        building = first_offer['building_info'][0]
        date_from = first_offer['start_time']
        date_to = first_offer['end_time']

        # save ONLY the first flexibility result from the algorithm to database
        response = {**response, 'offers': [response['offers'][0]]}

        data = {'type': 'flexibility_offer_confirmation_request',
                'user_id': user_id,
                'algorithm_response': response,
                'access_token': access_token}
        client.post('/flexibility_offer_confirmation/',
                    json.dumps(data),
                    content_type="application/json")

        # as Beyond, request the saved data for the aggregator
        data = {'type': 'flexibility_offer_by_aggregator',
                'start_time': date_from,
                'end_time': date_to,
                'user_id': user_id}
        signature = cryptography_wrapper.sign(mocks.BEYOND_PRIVATE_KEY, data)
        data = {**data, 'signature': signature}
        response = client.post('/flexibility_offer/',
                               json.dumps(data),
                               content_type="application/json").json()
        assert response['status'] is True

        # as Beyond, request the saved data for a building
        data = {'type': 'flexibility_offer_by_building',
                'start_time': date_from,
                'end_time': date_to,
                'building_id': building['building_id']}
        signature = cryptography_wrapper.sign(mocks.BEYOND_PRIVATE_KEY, data)
        data = {**data, 'signature': signature}
        response = client.post('/flexibility_offer/',
                               json.dumps(data),
                               content_type="application/json").json()
        assert response['status'] is True
