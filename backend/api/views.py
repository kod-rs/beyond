from django.db import models
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView

from backend.api.keycloak.keycloak_manager import keycloak_obtain_token


# todo write custom auth
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/

class IndexView(APIView):

    def get(self, request):

        response = {
            "auth": {
                "status": True,
                "access-token": request.access_token,
                "refresh-token": request.refresh_token
            },
            "payload": {
                "page": "index"
            }
        }

        return JsonResponse(response)


class Person(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class PersonSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)

        instance.save()
        return instance


class MapView(APIView):

    def post(self, request):

        print(f"{request.user=}")
        print(f"{request.auth=}")
        print(request.data)

        username = request.data["username"]
        password = request.data["password"]

        res = keycloak_obtain_token(username, password)

        # todo move to authenticate, enable in settings

        if all((i in res) for i in
               ["access_token", "expires_in", "refresh_expires_in",
                "refresh_token", "token_type", "id_token"]):
            access_token = res["access_token"]
            refresh_token = res["refresh_token"]

            response = {
                "ok": True,

                # "id": "user.id",

                "username": username,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        else:
            response = {
                "ok": False,

            }

        return JsonResponse(response)



