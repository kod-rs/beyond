from django.db import models


class Colour(models.Model):
    name = models.CharField(max_length=200, unique=False)
    hex = models.CharField(max_length=200, unique=False)
