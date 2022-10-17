import sys

from django.http import JsonResponse

from backend_old.api.comm.comm import bytes_to_json, get_empty_response_template
from backend_old.api.comm.json_loader import vue_interface_cfg
from backend_old.api.middleware.comm import DebuggableMiddleware
from backend_old.api.role_action_validation.args_check import check_params


class MsgBodyCheckMiddleware(DebuggableMiddleware):

    def __init__(self, get_response):
        super().__init__(get_response)

        self.vue_interface_cfg = vue_interface_cfg

    def __call__(self, request):
        print("MsgBodyCheckMiddleware")

        got_method = request.method
        got_headers = {}
        got_body = {}

        # fixme use meta?
        if request.headers:
            got_headers = request.headers

            got_headers = {k for k, v in got_headers.items()}
        if request.body:
            got_body = bytes_to_json(request.body)

            got_body = {k for k, v in got_body.items()}

        # todo uncomment,
        # t = check_params(
        #     path=request.path,
        #     method=got_method,
        #     headers_got=got_headers,
        #     body_got=got_body
        #
        # )
        #
        # if not t:
        #     print(80 * "-")
        #     sys.exit(-1)
        #     rejection = get_empty_response_template()
        #     return JsonResponse(rejection)

        # rejection = get_empty_response_template()
        #
        # if request.environ['QUERY_STRING'] != '':
        #     print('query string not empty')
        #     return JsonResponse(rejection)

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
