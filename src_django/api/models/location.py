from django.db import models


class Location(models.Model):
    location_id = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
