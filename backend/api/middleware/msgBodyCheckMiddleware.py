import json

from decouple import config
from django.http import JsonResponse

from backend.api.middleware.comm import get_empty_response_template, middleware_check_params
from backend.api.comm.json_loader import vue_interface_cfg
from backend.api.middleware.comm import DebuggableMiddleware

class MsgBodyCheckMiddleware(DebuggableMiddleware):
    def __init__(self, get_response):

        # self.get_response = get_response
        # self.debug = config("DEBUG") != "0"
        super().__init__(get_response)
        self.vue_interface_cfg = vue_interface_cfg

    def __call__(self, request):


        rejection = get_empty_response_template()

        if request.environ['QUERY_STRING'] != '':
            print('query string not empty')
            return JsonResponse(rejection)

        try:

            body = json.loads(request.body)
            keys = list(body.keys())

            # print("MsgBodyCheckMiddleware")
            #
            # print(request.action)
            # print(f"{keys=}")

            # todo

            #
            # print(str(request.get_full_path).strip("/"))

            t = request.path
            t = str(request.path).strip("/")

            # print(t)

            t = middleware_check_params(

                vue_interface_cfg=self.vue_interface_cfg,
                # route=request.action.split(";")[0],
                c=request.action,
                given=keys
            )

            print("check params", t)

            if not t:
                return JsonResponse(rejection)

            # if request.path == '/csrf/':
            #     if keys != ['access_token', 'refresh_token', 'action']:
            #         print('rejected csrf')
            #         return JsonResponse(rejection)
            #
            # elif request.path == '/locations/':
            #     expected_keys = ['access_token', 'refresh_token', 'action']
            #     if body['action'] == LOCATION_ACTION.DELETE_SINGLE.value:
            #         expected_keys.append('index')
            #     if body['action'] == LOCATION_ACTION.ADD_SINGLE.value:
            #         expected_keys += [
            #             "username",'type',
            #                           'section',
            #                           'latitude',
            #                           'longitude',
            #                           'synchronizer_token']
            #
            #     if keys != expected_keys:
            #         print(f"{keys=}")
            #         print(f"{expected_keys=}")
            #         print('rejected locations')
            #         return JsonResponse(rejection)
            #
            # elif request.path == '/login/':
            #     if keys != ['username', 'password']:
            #         print('rejected login')
            #         return JsonResponse(rejection)
            #
            # elif request.path == '/logout/':
            #     if list(body.keys()) != ['access_token', 'refresh_token']:
            #         print('rejected logout')
            #         return JsonResponse(rejection)

            return self.get_response(request)
        except Exception as e:
            if self.debug:
                print(e)
            print('rejected because of error')
            return JsonResponse(rejection)
