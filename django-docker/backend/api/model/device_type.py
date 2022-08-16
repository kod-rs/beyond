from django.db import models


class DeviceType(models.Model):
    value = models.CharField(max_length=200)
