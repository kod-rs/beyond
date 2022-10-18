from django.db import models

from src_django.api.models.location import Location
from src_django.api.models.person import Person


class PersonLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
