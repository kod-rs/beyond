from django.db import models


class CSRF(models.Model):
    ip = models.CharField(max_length=200, unique=True)
    synchronizer_token = models.CharField(max_length=2000, blank=True, null=True)
    encrypted_token = models.CharField(max_length=2000, blank=True, null=True)
    double_submitted_cookie = models.CharField(max_length=2000, blank=True, null=True)