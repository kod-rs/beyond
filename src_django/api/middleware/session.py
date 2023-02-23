import datetime
from django.utils import timezone
from src_django.api import common
from src_django.api.controller import user_sess


class CustomSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._mapping = common.internal_requests_mapping

    def __call__(self, request):
        request_body = common.json_decode(request.body)
        if request_body.get('type') in common.token_types:
            if not request_body.get('access_token'):
                return common.false_status(self._mapping[request_body.get('type')], 'token fail')
            # read from db GET EXP_TIME WHERE TOKEN = REQ(TOKEN)) (kroz dj)
            sess_data = user_sess.get_by_token(
                user_token=request_body['access_token'])

            if not sess_data:
                return common.false_status(self._mapping[request_body.get('type')], 'token fail')

            sess_expiry, sess_start = sess_data
            expiry_time = sess_start + datetime.timedelta(seconds=sess_expiry)
            if timezone.now() >= expiry_time:
                return common.false_status(self._mapping[request_body.get('type')], 'session expired')
            # check token expiry
            # if not sess_expiry:
            #     session_key = request.META.get(
            #         "HTTP_%s" % settings.SESSION_KEY_NAME,
            #         None)
            #     request.session = self.SessionStore(session_key)
        # Ako je apsolutno sve okej onda vracam zadnju liniju
        return self.get_response(request)
