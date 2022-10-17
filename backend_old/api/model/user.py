from django.db import models

class User(models.Model):

    zoomUserLocation = models.BooleanField()
    username = models.CharField(max_length=200, blank=True, null=True)

    # portfolio = models.CharField(max_length=200, blank=True, null=True)
