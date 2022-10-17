from decouple import config

from backend_old.api.cqrs_q.csrf import get_by_ip
from backend_old.api.comm.comm import bytes_to_json

class CSRFCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def __call__(self, request):
        print("CSRFCheckMiddleware")

        ip = request.ip
        pl = get_by_ip(ip)

        # todo
        # print(pl.synchronizer_token)
        # print(pl.encrypted_token)
        # print(pl.double_submitted_cookie)

        auth_credentials = {
            "synchronizer_token": None,
            "synchronizer-token": None,

        }

        if request.headers:

            for k, v in auth_credentials.items():
                if k in request.headers:
                    auth_credentials[k] = request.headers[k]

        if request.body:
            body_content = bytes_to_json(request.body)

            for k, v in auth_credentials.items():
                if k in body_content:
                    auth_credentials[k] = body_content[k]

        # todo refactor when impl other
        request.synchronizer_token_match = True
        # if hasattr(pl,"synchronizer_token" ) and ( (auth_credentials["synchronizer_token"] == pl.synchronizer_token) or (auth_credentials["synchronizer-token"] == pl.synchronizer_token)):
        #     print("\tmatch for synchronizer_token_match")
        #     request.synchronizer_token_match = True
        # else:
        #     print("\tno match for synchronizer_token_match")
        #     request.synchronizer_token_match = False

        return self.get_response(request)
