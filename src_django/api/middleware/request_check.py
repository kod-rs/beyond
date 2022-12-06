from src_django.api import common


class RequestCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._requests = common.internal_requests_mapping.keys()

    def __call__(self, request):
        # TODO
        # request_body = common.json_decode(request.body)
        # request_type = request_body.get('type')
        # if not request_type:
        #     print('Middleware: no request type')
        #     return
        # if request_type not in self._requests:
        #     print('Middleware: invalid request type')
        #     return
        return self.get_response(request)
