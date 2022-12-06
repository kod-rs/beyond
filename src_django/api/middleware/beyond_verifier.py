from pathlib import Path

from src_django.api import common
from src_django.api import cryptography_wrapper
from src_django.api.common import beyond_requests_mapping
from src_django.settings import BEYOND_CONFIG


class BeyondVerifierMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._beyond_requests_mapping = beyond_requests_mapping
        path = Path(BEYOND_CONFIG['BEYOND_PUBLIC_KEY_PATH'])
        key_bytes = cryptography_wrapper.load_public_key(path)
        key = cryptography_wrapper.get_public_key_from_bytes(key_bytes)
        self._beyond_public_key = key

    def __call__(self, request):

        request_body = common.json_decode(request.body)

        # Ignore if not Beyond type
        if request_body.get('type') not in self._beyond_requests_mapping:
            return self.get_response(request)

        # Get response based on request
        response_type = self._beyond_requests_mapping[request_body['type']]

        if not request_body.get('signature'):
            return common.false_status(response_type, 'no signature found')

        verified = cryptography_wrapper.verify_signature(
            self._beyond_public_key,
            request_body)

        if not verified:
            return common.false_status(response_type, 'validation fail')

        return self.get_response(request)
