from django.db import models

from playground.ic.backend_old.api.model.location import Location


class TemperatureValues(models.Model):
    # id
    value     = models.FloatField()


class TemperatureEntry(models.Model):

    # alt composite prim key
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    value = models.ForeignKey(
        TemperatureValues,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp = models.DateTimeField(auto_now_add=True)
