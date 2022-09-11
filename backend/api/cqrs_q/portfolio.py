from backend.api.model.portfolio import Portfolio
from backend.api.model.location import Location
from django.core import serializers


def get_portfolio(username, portfolio_name):
    return Portfolio.objects.get(username=username, name=portfolio_name)


def get_portfolios(username):

    try:
        return {"exists": True, "payload": Portfolio.objects.filter(username=username)}

    except Portfolio.DoesNotExist:
        return {"exists": False}


# def get_portfolios_with_locations(username):
#
#     try:
#         return Location.objects.filter(portfolio__username=username)
#
#     except Portfolio.DoesNotExist:
#         return False

# def get_portfolio_names(username):
#     # fixme what if no portfolios
#
#     try:
#         return Portfolio.objects.filter(username=username).only("name")
#
#     except Portfolio.DoesNotExist:
#         return False
