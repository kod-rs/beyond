from django.db import models

from backend.api.model.location import Location


class TemperatureValues(models.Model):
    # id
    value     = models.FloatField()


class TemperatureEntry(models.Model):

    # alt composite prim key
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    # values
    value = models.ForeignKey(
        TemperatureValues,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    # colour = models.CharField(max_length=20, blank=True, null=True)

