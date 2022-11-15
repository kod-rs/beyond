from django.db import models


class BuildingFlexibility(models.Model):
    building_id = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flexibility = models.FloatField()
