from django.db import models

class IpCounter(models.Model):

    ip = models.CharField(max_length=200)
    counter = models.IntegerField()
