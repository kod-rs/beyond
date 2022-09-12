from backend.api.model.location import Location


def get_user_portfolio(username, portfolio_name):

    return Location.objects.filter(
        portfolio__username=username,
        portfolio__name=portfolio_name
    )




