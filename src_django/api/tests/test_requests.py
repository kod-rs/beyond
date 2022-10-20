import json

from django.test import Client
from django.test import TestCase

from src_django.api.tests import common


class TestLocation(TestCase):
    def setUp(self):
        common.populate_database()

    def test_get_portfolios(self):
        client = Client()
        data = {'user_id': 1}
        response = client.post('/portfolio/',
                               json.dumps(data),
                               content_type="application/json")
        assert response.json()['status'] is True
        assert len(response.json()['portfolios']) == 2

    def test_get_locations_for_portfolio(self):
        client = Client()
        data = {'portfolio_id': 101}
        response = client.post('/location/',
                               json.dumps(data),
                               content_type="application/json")
        assert response.json()['status'] is True
        assert len(response.json()['locations']) == 3
