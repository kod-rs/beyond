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


# view?
from django.http import JsonResponse
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

        user = authenticate(request, username=username, password=password)

        responseJson = {
            "ok": True,
            "id": "user.id",
            "username": "user.username",
            "firstName": "user.firstName",
            "lastName": "user.lastName"
        }

        return JsonResponse(responseJson)

        # if not user:
        #

        #     return JsonResponse({'is_auth_correct': False})
        #
        # else:
        #     return JsonResponse({'is_auth_correct': True})


from rest_framework import viewsets, views
from . import models
    # , serializers
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.exceptions import PermissionDenied

class BankViewSet(viewsets.ModelViewSet):
    """
    Bank endpoint
    This endpoint has all configured keycloak roles
    """
    # serializer_class = serializers.BankSerializer
    # queryset = models.Bank.objects.all()
    keycloak_roles = {
        'GET': ['director', 'judge', 'employee'],
        'POST': ['director', 'judge', ],
        'UPDATE': ['director', 'judge', ],
        'DELETE': ['director', 'judge', ],
        'PATCH': ['director', 'judge', 'employee'],
    }

    def list(self, request):
        """
        Overwrite method
        You can especify your rules inside each method
        using the variable 'request.roles' that means a
        list of roles that came from authenticated token.
        See the following example bellow:
        """
        # list of token roles
        print(request.roles)

        # Optional: get userinfo (SUB attribute from JWT)
        print(request.userinfo)

        return super().list(self, request)


class CarViewSet(viewsets.ViewSet):
    """
    Car endpoint
    This endpoint has not configured keycloak roles.
    That means all methods will be allowed to access.
    """
    def list(self, request):
        return JsonResponse({"detail": "success"}, status=status.HTTP_200_OK)


class JudgementView(views.APIView):
    """
    Judgement endpoint
    This endpoint has configured keycloak roles only GET method.
    Other HTTP methods will be allowed.
    """
    keycloak_roles = {
        'GET': ['judge'],
    }

    def get(self, request, format=None):
        """
        Overwrite method
        You can especify your rules inside each method
        using the variable 'request.roles' that means a
        list of roles that came from authenticated token.
        See the following example bellow:
        """
        # list of token roles
        print(request.roles)

        # Optional: get userinfo (SUB attribute from JWT)
        print(request.userinfo)

        return super().get(self, request)

# http://127.0.0.1:8000/api/callback