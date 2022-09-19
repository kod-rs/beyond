from django.db import models


class ColourHistory(models.Model):
    colour = models.CharField(max_length=20, blank=True, null=True)

