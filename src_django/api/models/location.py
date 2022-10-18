from django.db import models


class Location(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
