from django.db import models


class UserSession(models.Model):
    """
    Database representation of user's session information

    Args:
        user_token: string that contains user's token
        expires_in: amount os seconds that session lasts
        session_start: user session start date time
    """
    user_token = models.CharField(max_length=2_000)
    expires_in = models.IntegerField()
    session_start = models.DateTimeField()
