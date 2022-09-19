from django.db import models


class NameHistory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

