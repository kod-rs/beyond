from django.db import models

from src_django.api.models.location import Location


class Data(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
