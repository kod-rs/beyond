from decouple import config

from backend.api.cqrs_q.csrf import get_by_ip
from backend.api.comm.comm import bytes_to_json

class JumperMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print("auto middleware")

        # fixme only for testing
        request.access_token = "tmp"
        request.refresh_token = "tmp"
        request.username = "a"
        request.ip = "127.0.0.1"
        request.synchronizer_token_match = True
        request.role = "role 1"

        return self.get_response(request)
