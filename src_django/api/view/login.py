import keycloak.exceptions
from django.http import JsonResponse
from keycloak import KeycloakOpenID
from rest_framework.views import APIView

from src_django.api.validator.internal_api.login import validate_internal_login
from src_django.api.view import common
from src_django.settings import KEYCLOAK_CONFIG


class LoginView(APIView):
    def __init__(self):
        super().__init__()
        self._openid = _keycloak_connect()
        self._request_type = 'login_request'
        self._response_type = 'login_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)

        if not validate_internal_login(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        try:
            token = self._openid.token(username=request_body['username'],
                                       password=request_body['password'])
            userinfo = self._openid.userinfo(token['access_token'])
        except keycloak.exceptions.KeycloakAuthenticationError as e:
            return common.false_status(msg=str(e.response_code),
                                       response_type=self._response_type)
        except keycloak.exceptions.KeycloakConnectionError:
            return common.false_status(msg='server connection error',
                                       response_type=self._response_type)
        except keycloak.exceptions.KeycloakPostError:
            return common.false_status(msg='account not fully set up',
                                       response_type=self._response_type)

        try:
            role = set(userinfo['realm_access']['roles'])
            role = role.intersection({'AGGREGATOR', 'MANAGER'})
            assert len(role) == 1
            role = role.pop()
            username = userinfo['preferred_username']
        except Exception:
            return common.false_status(
                msg='invalid data received from keycloak',
                response_type=self._response_type)

        return JsonResponse({'type': self._response_type,
                             'status': True,
                             'user_id': userinfo['sub'],
                             'username': username,
                             'role': role,
                             'access_token': token['refresh_token']})


def _keycloak_connect():
    keycloak_openid = KeycloakOpenID(
        server_url=KEYCLOAK_CONFIG['URL'],
        client_id=KEYCLOAK_CONFIG['CLIENT_ID'],
        realm_name=KEYCLOAK_CONFIG['REALM_NAME'],
        client_secret_key=KEYCLOAK_CONFIG['CLIENT_SECRET_KEY'])
    return keycloak_openid
