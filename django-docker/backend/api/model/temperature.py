from django.db import models


class Device(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    value = models.FloatField()