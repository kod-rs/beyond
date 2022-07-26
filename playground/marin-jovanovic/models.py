# from django.db import models
# from rest_framework import serializers
#
#
# class Message(models.Model):
#     subject = models.CharField(max_length=200)
#     body = models.TextField()
#
#
# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Message
#         fields = ('url', 'subject', 'body', 'pk')
#
# ##################################################################
#
#
# class User(models.Model):
#
#     class Role(models.IntegerChoices):
#         AGGREGATOR = 1
#         BUILDING_MANAGER = 2
#         AGGREGATOR_AND_BUILDING_MANAGER = 3
#
#     role_id = models.IntegerField(choices=Role.choices)
#     password = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)


# from .models import Message, MessageSerializer

# class MessageViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer