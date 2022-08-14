from django.db import models


class Location(models.Model):
    username = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
