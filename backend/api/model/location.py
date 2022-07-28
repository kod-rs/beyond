from django.db import models


class Location(models.Model):
    section = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)