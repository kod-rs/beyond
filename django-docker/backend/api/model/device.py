from django.db import models


class Device(models.Model):
    data_id = models.PositiveIntegerField()
    type_id = models.PositiveIntegerField()
    consumption = models.FloatField()
