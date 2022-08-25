from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=200, unique=False)
    user_username = models.CharField(max_length=200, unique=False)
