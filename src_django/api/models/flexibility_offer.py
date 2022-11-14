from django.db import models


class Portfolio(models.Model):
    username = models.CharField(max_length=200, unique=False)
    name = models.CharField(max_length=200, unique=False)
