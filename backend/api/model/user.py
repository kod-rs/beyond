from django.db import models


class User(models.Model):
    portfolio = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    history_colour_id = models.CharField(max_length=200, blank=True, null=True)
    timestamp_colour_change = models.DateTimeField(auto_now_add=True)
