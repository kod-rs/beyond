import json
from django.http import JsonResponse
from backend.api.middleware.comm import middleware_check_params
from backend.api.comm.http import get_empty_response_template
from backend.api.comm.json_loader import vue_interface_cfg
from backend.api.middleware.comm import DebuggableMiddleware


class MsgBodyCheckMiddleware(DebuggableMiddleware):

    def __init__(self, get_response):
        super().__init__(get_response)

        self.vue_interface_cfg = vue_interface_cfg

    def __call__(self, request):
        print("MsgBodyCheckMiddleware")
        # rejection = get_empty_response_template()
        #
        # if request.environ['QUERY_STRING'] != '':
        #     print('query string not empty')
        #     return JsonResponse(rejection)
        #
        # # todo
        # # try:
        #
        # body = json.loads(request.body)
        # keys = list(body.keys())
        #
        # if not middleware_check_params(
        #     action_composite=request.action,
        #     given=keys
        # ):
        #     print(f"\tmissing something, {request.action=}")
        #     print(f"\tprovided {keys}")
        #     # return JsonResponse(rejection)

        return self.get_response(request)

        # except Exception as e:
        #     if self.debug:
        #         print(e)
        #         print('rejected because of error')
        #
        # return JsonResponse(rejection)
