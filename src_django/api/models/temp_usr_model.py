from django.db import models


class TempUserModel(models.Model):
    user_token = models.CharField(max_length=2_000)
    user_id = models.CharField(max_length=2_000, unique=True)
    username = models.CharField(max_length=2_000)
