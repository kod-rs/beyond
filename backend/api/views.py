import json
import random

from django.http import Http404
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer
from rest_framework.views import APIView
from rest_framework import serializers
from django.db import models


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


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

from django.http import JsonResponse
class SnippetDetail(APIView):

    def post(self, request, pk):
        print(f"{request.user=}")
        print(f"{request.auth=}")

        username = request.data["username"]
        password = request.data["password"]
        role = request.data["role"]

        print(username)

        from random import randint
        is_auth_correct = randint(0,1)

        if is_auth_correct:
            return JsonResponse({'foo': 'bar'})
        else:
            return JsonResponse({'foo': 'no'})
