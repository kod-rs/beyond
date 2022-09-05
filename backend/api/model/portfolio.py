from django.db import models
from backend.api.model.colour import Colour


class Portfolio(models.Model):
    name = models.CharField(max_length=200, unique=False)
    username = models.CharField(max_length=200, unique=False)
    # colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    colour = models.CharField(max_length=200, unique=False)
