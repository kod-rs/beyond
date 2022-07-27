from django.db import models


class Device(models.Model):
    # fixme check how to connect
    # device_id = models.AutoField()
    # fixme number?
    data_id = models.CharField(max_length=200)
    # fixme enum?
    device_type = models.CharField(max_length=200)
    # fixme type?
    consumption = models.CharField(max_length=200)
