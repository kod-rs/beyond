from django.db import models


# changed from building to location
class Location(models.Model):
    # building_id = models.AutoField()
    # todo check if enum
    building_type =models.CharField(max_length=200)
    # todo check if enum
    section =models.CharField(max_length=200)
    # todo check if geotag
    # geo =

    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)