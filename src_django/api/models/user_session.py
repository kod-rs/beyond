from django.db import models


class UserSession(models.Model):
    """
    Database representation of user's session information

    Args:
        user_id: string unique to each user
        user_token: string that contains user's token
        expires_in: amount os seconds that session lasts
    """
    user_id = models.CharField(max_length=200)
    user_token = models.CharField()
    expires_in = models.IntegerField()
