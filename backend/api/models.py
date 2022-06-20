from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

##################################################################

class User(models.Model):

    class Role(models.IntegerChoices):
        AGGREGATOR = 1
        BUILDING_MANAGER = 2

    role_id = models.IntegerField(choices=Role.choices)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
