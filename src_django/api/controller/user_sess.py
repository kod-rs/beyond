import datetime

from src_django.api.models import UserSession


def add(user_token: str,
        expires_in: int, session_start: datetime.datetime) -> bool:
    """
    Saves user session information to database

    Args:
        user_token: unique user token
        expires_in: amount of time that session lasts
        session_start: user session date time

    Returns:
        True if saving was successful, False otherwise
    """
    try:
        new_user_session = UserSession(user_token=user_token,
                                       expires_in=expires_in,
                                       session_start=session_start)
        new_user_session.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True


def get_by_token(user_token: str
                 ) -> tuple[int, datetime.datetime] | bool:
    """
    Reads data from database based on user ID and user token

    Args:
        user_token: unique user token

    Returns:
        User session expiry time in seconds
    """
    try:
        query_res = UserSession.objects.get(user_token=user_token)
        return query_res.expires_in, query_res.session_start
    except Exception as e:
        print(f'error={e}')
        return False
