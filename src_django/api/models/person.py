from django.db import models


class RoleChoices(models.TextChoices):
    MANAGER = 'manager'
    AGGREGATOR = 'aggregator'


class Person(models.Model):
    role = models.TextField(choices=RoleChoices.choices)
