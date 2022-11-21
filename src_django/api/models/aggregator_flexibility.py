from django.db import models


class AggregatorFlexibility(models.Model):
    """
    Database representation of flexibility offered by an aggregator
    Args:
        user_id: string unique to each user
        start_time: time that the offered flexibility can start
        end_time: time that the offered flexibility ends
        flexibility: amount of offered flexibility
    """
    user_id = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flexibility = models.FloatField()
