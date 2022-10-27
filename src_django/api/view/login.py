import json

import keycloak.exceptions
from django.http import JsonResponse
from keycloak import KeycloakOpenID
from rest_framework.views import APIView

from src_django.api.view import common
from src_django.settings import KEYCLOAK_CONFIG


class LoginView(APIView):
    def __init__(self):
        super().__init__()
        self._openid = _keycloak_connect()
        self._response_type = 'login_response'

    def post(self, request) -> JsonResponse:
        credentials = json.loads(request.body)
        reason = credentials.get('type')
        username = credentials.get('username')
        password = credentials.get('password')

        if not username or not password or reason != 'login_request':
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)
        try:
            token = self._openid.token(username=username, password=password)
            userinfo = self._openid.userinfo(token['access_token'])
        except keycloak.exceptions.KeycloakAuthenticationError as e:
            return common.false_status(msg=str(e.response_code),
                                       response_type=self._response_type)
        except keycloak.exceptions.KeycloakConnectionError:
            return common.false_status(msg='server connection error',
                                       response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True,
                             'user_id': userinfo['sub'],
                             'access_token': token['refresh_token']})


def _keycloak_connect():
    keycloak_openid = KeycloakOpenID(
        server_url=KEYCLOAK_CONFIG['URL'],
        client_id=KEYCLOAK_CONFIG['CLIENT_ID'],
        realm_name=KEYCLOAK_CONFIG['REALM_NAME'],
        client_secret_key=KEYCLOAK_CONFIG['CLIENT_SECRET_KEY'])
    return keycloak_openid
