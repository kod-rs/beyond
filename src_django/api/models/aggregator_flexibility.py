from django.db import models


class AggregatorFlexibility(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flexibility = models.FloatField()
