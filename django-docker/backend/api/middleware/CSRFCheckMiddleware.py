from backend.api.comm.comm import decode_data
from backend.api.cqrs_q.csrf import get_by_ip


class CSRFCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.ip
        pl = get_by_ip(ip)
        auth_credentials = {"synchronizer_token": None,
                            "synchronizer-token": None}

        if request.headers:
            for k, v in auth_credentials.items():
                if k in request.headers:
                    auth_credentials[k] = request.headers[k]

        if request.body:
            body_content = decode_data(request.body)
            for k, v in auth_credentials.items():
                if k in body_content:
                    auth_credentials[k] = body_content[k]

        if (hasattr(pl, "synchronizer_token")
                and ((auth_credentials[
                          "synchronizer_token"] == pl.synchronizer_token)
                     or (auth_credentials[
                             "synchronizer-token"] == pl.synchronizer_token))):
            request.synchronizer_token_match = True
        else:
            request.synchronizer_token_match = False

        return self.get_response(request)
