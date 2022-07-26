from django.db import models

class PemKeys(models.Model):

    key_type = models.CharField(max_length=200)
    key_value = models.CharField(max_length=2000)
