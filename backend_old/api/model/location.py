from django.db import models
from backend_old.api.model.portfolio import Portfolio


class Location(models.Model):
    # alternative key
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    section = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
