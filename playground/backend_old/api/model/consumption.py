from django.db import models

from playground.backend_old.api.model.location import Location


class consumptionValues(models.Model):
    # id
    value = models.FloatField()


class consumptionEntry(models.Model):
    # alt composite prim key
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    value = models.ForeignKey(
        consumptionValues,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    # value
    timestamp = models.DateTimeField(auto_now_add=True)
