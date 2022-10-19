from playground.ic.backend_old.api.model.portfoliocolouradapter import PortfolioColourAdapter


def get_colour_log(user, portfolio):

    t = PortfolioColourAdapter\
        .objects\
        .filter(portfolio__username=user, portfolio__name=portfolio)\
        .select_related("history_colour_id")\
        .order_by('-timestamp')
    return t
