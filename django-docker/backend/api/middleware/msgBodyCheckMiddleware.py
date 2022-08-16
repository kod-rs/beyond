import json

from django.http import JsonResponse

from backend.api.config.main import ACTIONS


class MsgBodyCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rejection = {"auth": {"status": False,
                              "access-token": "",
                              "refresh-token": ""},
                     "payload": {},
                     "debug": ""}
        try:
            body = json.loads(request.body)
            keys = list(body.keys())

            if request.environ['QUERY_STRING'] != '':
                return JsonResponse(rejection)

            if request.path == '/csrf/':
                if keys != ['access_token', 'refresh_token', 'action']:
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
                    return JsonResponse(rejection)

            elif request.path == '/login/':
                if keys != ['username', 'password']:
                    return JsonResponse(rejection)

            elif request.path == '/logout/':
                if list(body.keys()) != ['access_token', 'refresh_token']:
                    return JsonResponse(rejection)

            return self.get_response(request)
        except Exception:
            return JsonResponse(rejection)
