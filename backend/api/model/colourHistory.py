from django.db import models


class ColourHistory(models.Model):
    colour_hex_value = models.CharField(max_length=20, blank=True, null=True)

