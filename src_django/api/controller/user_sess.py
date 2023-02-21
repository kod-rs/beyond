import typing

from src_django.api.models import UserSession


def add(user_id: str, user_token: str, expires_in: int) -> bool:
    """
    Saves user session information to database

    Args:
        user_id: unique user ID
        user_token: unique user token
        expires_in: amount of time that session lasts

    Returns:
        True if saving was successful, False otherwise
    """
    try:
        new_user_session = UserSession(user_id=user_id,
                                       user_token=user_token,
                                       expires_in=expires_in)
        new_user_session.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True


def get_by_usr_and_token(user_id: str, user_token: str) -> int:
    """
    Reads data from database based on user ID and user token

    Args:
        user_id: unique user id
        user_token: unique user token

    Returns:
        User session expiry time in seconds
    """
    try:
        query_res = UserSession.objects.get(user_id=user_id,
                                            user_token=user_token)
        return query_res.expires_in
    except Exception as e:
        print(f'error={e}')
        return False
