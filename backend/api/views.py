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

        print(f"{request.user=}")
        print(f"{request.auth=}")

        # t = HttpRequest.read(request)
        # print("t je  ", t)

        username = request.data["username"]
        password = request.data["password"]
        print(f"{username=}")
        print(f"{password=}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({'is_auth_correct': 'yes'})

            # login(request, user)
            # Redirect to a success page.
            ...
        else:
            return JsonResponse({'is_auth_correct': 'no'})
            # Return an 'invalid login' error message.
            # ...

        # print(request.data)
        #
        #
        # from random import randint
        # is_auth_correct = randint(0,1)
        #
        # # return JsonResponse({'is_auth_correct': is_auth_correct} + request.data)
        #
        # if is_auth_correct:
        #     return JsonResponse({'is_auth_correct': 'yes'})
        # else:
        #     return JsonResponse({'is_auth_correct': 'no'})
