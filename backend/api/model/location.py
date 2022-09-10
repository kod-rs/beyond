from django.db import models
from backend.api.model.portfolio import Portfolio


class Location(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)

    section = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
