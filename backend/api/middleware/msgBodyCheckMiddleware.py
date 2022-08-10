import json

from decouple import config
from django.http import JsonResponse

from backend.api.config.main import ACTIONS


class MsgBodyCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        if self.debug:
            print(80 * "-")
            print("\tMsgBodyCheckMiddleware")
        rejection = {"auth": {"status": False,
                              "access-token": "",
                              "refresh-token": ""},
                     "payload": {},
                     "debug": ""}
        try:
            body = json.loads(request.body)
            keys = list(body.keys())

            if request.path == '/csrf/':
                if keys != ['access_token', 'refresh_token', 'action']:
                    print('rejected csrf')
                    return JsonResponse(rejection)

            elif request.path == '/locations/':
                expected_keys = ['access_token', 'refresh_token', 'action']
                if body['action'] == ACTIONS.DELETE.value:
                    expected_keys.append('index')
                if body['action'] == ACTIONS.ADD.value:
                    expected_keys += ['type',
                                      'section',
                                      'latitude',
                                      'longitude',
                                      'synchronizer_token']
                if keys != expected_keys:
                    print('rejected locations')
                    return JsonResponse(rejection)

            elif request.path == '/login/':
                if keys != ['username', 'password']:
                    print('rejected login')
                    return JsonResponse(rejection)

            elif request.path == '/logout/':
                if list(body.keys()) != ['access_token', 'refresh_token']:
                    print('rejected logout')
                    return JsonResponse(rejection)

            return self.get_response(request)
        except Exception as e:
            if self.debug:
                print(e)
            print('rejected because of error')
            return JsonResponse(rejection)
