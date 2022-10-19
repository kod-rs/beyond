from django.db import models

from src_django.api.models.location import Location
from src_django.api.models.portfolio import Portfolio


class PortfolioLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
