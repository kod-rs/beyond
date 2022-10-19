import json

from django.test import Client
from django.test import TestCase

from src_django.api.tests import common


class TestLocation(TestCase):
    def setUp(self):
        common.set_up_locations()

    def test_location_get(self):
        client = Client()
        data = {'location_ids': ['ABC1', 'ABC2', 'ABC3']}
        response = client.post('/location/',
                               json.dumps(data),
                               content_type="application/json")
        assert response.json()['status'] is True
        assert len(response.json()['locations']) == 2
