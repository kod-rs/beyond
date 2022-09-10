from backend.api.model.portfoliocolouradapter import PortfolioColourAdapter


def get_colour_log(user, portfolio):

    t = PortfolioColourAdapter\
        .objects\
        .filter(portfolio=portfolio, username=user)\
        .select_related("history_colour_id")\
        .order_by('-timestamp_colour_change')
    return t
