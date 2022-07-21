import json
import random

from django.http import Http404, HttpRequest
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer
from rest_framework.views import APIView
from rest_framework import serializers
from django.db import models
from django.http import JsonResponse

# todo write custom auth
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
from django.contrib.auth import authenticate, login


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# model
class Person(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)



# for data representation
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


class SnippetDetail(APIView):

    # used when passing args coded in url, not as args, ie pagination
    # def post(self, request, pk):
    def post(self, request):
        print("post login")

        print(f"{request.user=}")
        print(f"{request.auth=}")

        print(request.data)

        username = request.data["username"]
        password = request.data["password"]

        from .keycloak_manager import keycloak_obtain_token
        res = keycloak_obtain_token(username, password)
        # access_token = res["access_token"]

        # todo move to authenticate, enable in settings

        if all((i in res) for i in ["access_token", "expires_in", "refresh_expires_in", "refresh_token", "token_type", "id_token"]):
            responseJson = {
                "ok": True,
                "id": "user.id",
                "username": username,
                "firstName": "user.firstName",
                "lastName": "user.lastName"
            }
        else:
            responseJson = {
                "ok": False,
                "id": "user.id",
                "username": username,
                "firstName": "user.firstName",
                "lastName": "user.lastName"
            }
        # print("res", res)

        # user = authenticate(request, username=username, password=password)


        return JsonResponse(responseJson)

        # if not user:
        #

        #     return JsonResponse({'is_auth_correct': False})
        #
        # else:
        #     return JsonResponse({'is_auth_correct': True})

