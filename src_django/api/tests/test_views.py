import datetime
import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api.models.aggregator_flexibility import AggregatorFlexibility
from src_django.api.models.building_flexibility import BuildingFlexibility
from src_django.api.tests import mocks
from src_django.api import common


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
    def test_algorithm(self):
        client = Client()

        date_from = datetime.datetime(year=2022, month=4, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc).isoformat()
        date_to = datetime.datetime(year=2022, month=4, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc).isoformat()
        flex_amount = 300
        data = {'type': 'algorithm_request',
                'building_energy_list': mocks.mock_building_energy_list(),
                'interval': {
                    'from': date_from,
                    'to': date_to},
                'flexibility_amount': flex_amount,
                'month': None}

        response = client.post('/algorithm/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'algorithm_response'
        assert response['status'] is True
        assert (isinstance(response['offered_flexibility'], float)
                or isinstance(response['offered_flexibility'], int))
        assert isinstance(response['building_info'], list)
        assert response['interval']['from'] == date_from
        assert response['interval']['to'] == date_to
        assert response['requested_flexibility'] == flex_amount
        assert response['offered_flexibility'] <= flex_amount
        assert isinstance(response['building_info'], list)
        assert len(response['building_info']) > 0
        building = response['building_info'][0]
        assert building['flexibility'] <= flex_amount
        assert building['interval']['from'] == date_from
        assert building['interval']['to'] == date_to


class TestFlexibilityOfferConfirmationView(TestCase):
    def test_flexibility_offer_confirmation(self):
        client = Client()

        date_from = datetime.datetime(year=2022, month=2, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc).isoformat()
        date_to = datetime.datetime(year=2022, month=2, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc).isoformat()
        interval = {'from': date_from, 'to': date_to}

        algorithm_response = {
            'building_info': [
                {'building_id': 'ZIV0034704030',
                 'flexibility': 95.8,
                 'interval': interval},
                {'building_id': 'ZIV0034902130',
                 'flexibility': 93.65,
                 'interval': interval}],
            'offered_flexibility': 189.45,
            'status': True,
            'interval': interval,
            'type': 'algorithm_response'}

        data = {'type': 'flexibility_offer_confirmation_request',
                'user_id': 'usr1',
                'algorithm_response': algorithm_response}

        response = client.post('/flexibility_offer_confirmation/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'flexibility_offer_confirmation_response'
        assert response['status'] is True


class TestFlexibilityOfferRequest(TestCase):
    def setUp(self):
        date_from = datetime.datetime(year=2022, month=2, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc)
        date_to = datetime.datetime(year=2022, month=2, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc)
        AggregatorFlexibility.objects.create(user_id='usr1',
                                             start_time=date_from,
                                             end_time=date_to,
                                             flexibility=420)
        BuildingFlexibility.objects.create(building_id='b1',
                                           start_time=date_from,
                                           end_time=date_to,
                                           flexibility=820)

        date_from = date_from.replace(hour=10)
        date_to = date_to.replace(hour=11)
        AggregatorFlexibility.objects.create(user_id='usr1',
                                             start_time=date_from,
                                             end_time=date_to,
                                             flexibility=440)
        BuildingFlexibility.objects.create(building_id='b1',
                                           start_time=date_from,
                                           end_time=date_to,
                                           flexibility=840)

        date_from = date_from.replace(hour=18)
        date_to = date_to.replace(hour=19)
        AggregatorFlexibility.objects.create(user_id='usr1',
                                             start_time=date_from,
                                             end_time=date_to,
                                             flexibility=421)
        BuildingFlexibility.objects.create(building_id='b1',
                                           start_time=date_from,
                                           end_time=date_to,
                                           flexibility=821)

    def test_flexibility_offer_request_agr(self):
        client = Client()

        date_from = datetime.datetime(year=2022, month=2, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc).isoformat()
        date_to = datetime.datetime(year=2022, month=2, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc).isoformat()

        data = {'type': 'flexibility_offer_by_aggregator',
                'start_time': date_from,
                'end_time': date_to,
                'user_id': 'usr1'}

        response = client.post('/flexibility_offer/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'flexibility_offer_by_aggregator_response'
        assert response['user_id'] == 'usr1'
        assert response['status'] is True
        assert isinstance(response['offered_flexibilities'], list)
        assert len(response['offered_flexibilities']) > 0
        flex = response['offered_flexibilities'][0]
        assert flex['flexibility'] > 0
        assert isinstance(datetime.datetime.fromisoformat(flex['end_time']),
                          datetime.datetime)

    def test_flexibility_offer_request_building(self):
        client = Client()

        date_from = datetime.datetime(year=2022, month=2, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc).isoformat()
        date_to = datetime.datetime(year=2022, month=2, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc).isoformat()

        data = {'type': 'flexibility_offer_by_building',
                'start_time': date_from,
                'end_time': date_to,
                'building_id': 'b1'}

        response = client.post('/flexibility_offer/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()

        assert response['type'] == 'flexibility_offer_by_building_response'
        assert response['building_id'] == 'b1'
        assert response['status'] is True
        assert isinstance(response['offered_flexibilities'], list)
        assert len(response['offered_flexibilities']) > 0
        flex = response['offered_flexibilities'][0]
        assert flex['flexibility'] > 0
        assert isinstance(datetime.datetime.fromisoformat(flex['end_time']),
                          datetime.datetime)
