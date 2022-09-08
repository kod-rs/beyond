from django.db import models
from django.contrib.postgres.fields import ArrayField

from backend.api.model.portfolio import Portfolio


class Colour(models.Model):

    # name = models.CharField(max_length=200, unique=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)
    hex_log =      ArrayField(
            models.CharField(max_length=7, blank=False),
            size=10,
        )
    # hex = models.CharField(max_length=200, unique=False)
