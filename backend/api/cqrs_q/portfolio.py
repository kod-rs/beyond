from backend.api.model.portfolio import Portfolio
from backend.api.model.location import Location
from django.core import serializers


def get_portfolios(username):

    try:
        return Portfolio.objects.filter(username=username)

    except Portfolio.DoesNotExist:
        return False


def get_portfolios_with_locations(username):

    try:

        ip_obj = Location.objects.filter(portfolio__username=username)
        print(f"{ip_obj=}")

        t = serializers.serialize('json', ip_obj)
        print(t)
        print("---")
        # for i in t:
        #     print(i)
        return ip_obj

    except Portfolio.DoesNotExist:
        return False

def get_portfolio_names(username):

    try:
        return Portfolio.objects.filter(username=username).only("name")

    except Portfolio.DoesNotExist:
        return False
