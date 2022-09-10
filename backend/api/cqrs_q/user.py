from backend.api.model.user import User


def get_colour_log(user, portfolio):

    t = User\
        .objects\
        .filter(portfolio=portfolio, username=user)\
        .select_related("history_colour_id")\
        .order_by('-timestamp_colour_change')
    return t
