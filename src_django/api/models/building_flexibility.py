from django.db import models


class BuildingFlexibility(models.Model):
    """
    Database representation of flexibility offered by a building
    Args:
        building_id: string unique to each building
        start_time: time that the offered flexibility can start
        end_time: time that the offered flexibility ends
        flexibility: amount of offered flexibility
    """
    building_id = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flexibility = models.FloatField()
