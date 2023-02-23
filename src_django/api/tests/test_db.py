import datetime
import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase

from src_django.api.controller import user_sess
from src_django.api.tests import mocks


class TestSessionEntry(TestCase):
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
        expiry, sess_start = user_sess.get_by_token(
            user_token=response['access_token'])

        assert isinstance(expiry, int)
        assert isinstance(sess_start, datetime.datetime)
