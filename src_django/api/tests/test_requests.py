import json
from unittest.mock import MagicMock

import keycloak
from django.test import Client
from django.test import TestCase


class TestLogin(TestCase):
    def setUp(self):
        def _token(username, password):
            if username == password == 'mirkofleks':
                return {'refresh_token': 'r3f75h',
                        'access_token': 'ac355_70k3n'}
            else:
                raise keycloak.exceptions.KeycloakAuthenticationError(
                    response_code=401)

        keycloak.KeycloakOpenID.token = MagicMock(
            side_effect=_token)
        keycloak.KeycloakOpenID.userinfo = MagicMock(
            return_value={'sub': '5u8'})

    def test_get_user_info(self):
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

        data['password'] = 'wrong_password'
        response = client.post('/login/',
                               json.dumps(data),
                               content_type="application/json")
        response = response.json()
        assert response['type'] == 'login_response'
        assert response['status'] is False
        assert response['message'] == '401'
