# TODO
# from django.conf import settings
# from django.contrib.sessions.middleware import SessionMiddleware
# from api.common import json_decode
# from importlib import import_module
# from src_django.api import common
#
#
# class CustomSessionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self._mapping = common.request_response_mapping
#
#     def __call__(self, request):
#         request_body = json_decode(request.body)
#         # if request_body.get('token'):
#         #     # check token expiry
#         #     # if expired
#         #
#         #     session_key = request.META.get(
#         #         "HTTP_%s" % settings.SESSION_KEY_NAME,
#         #         None)
#         #     request.session = self.SessionStore(session_key)
#         return self.get_response(request)
