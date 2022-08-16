from django.db import models


class Data(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    value = models.FloatField()
    is_predicted = models.BooleanField()
    location_id = models.PositiveIntegerField()
