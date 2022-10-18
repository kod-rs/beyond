from django.db import models


class RoleChoices(models.TextChoices):
    MANAGER = 'manager'
    AGGREGATOR = 'aggregator'


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.TextField(choices=RoleChoices.choices)
