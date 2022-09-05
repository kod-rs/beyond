import urllib

from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from backend.api.authenticate import login, check_tokens

import datetime
from django.utils import timezone


class KeycloakBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        print("KeycloakBackend")

        if "HTTP_AUTHORIZATION" not in request.META:
            # print("no authorization")
            return None

        authorization_header = request.META['HTTP_AUTHORIZATION']
        parsed_authorization_header = urllib.parse.unquote(authorization_header)
        auth_type, payload = parsed_authorization_header.split(" ")

        if auth_type == "Basic":
            # print("user pass")
            username, password = payload.split(":")
            res = login(username, password)

        elif auth_type == "Digest":
            # print("Digest")

            # todo https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
            access_token, refresh_token = payload.split(":")
            res = check_tokens(access_token, refresh_token)

        else:
            res = {"is_valid": False}

        if not res["is_valid"]:
            # print("user pass err")
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_superuser = False
            user.is_staff = False

            # todo
            user.password = "None"
            user.first_name = "None"
            user.last_name = "None"
            user.email = "None"

        user.last_login = timezone.now()
        user.is_active = True
        user.save()

        request.username = username
        request.access_token = res["access_token"]
        request.refresh_token = res["refresh_token"]
        request.is_auth = True

        # print(f"{user=}")
        return User


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

