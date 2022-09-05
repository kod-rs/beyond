from backend.api.model.portfolio import Portfolio
from backend.api.model.location import Location
from django.core import serializers


def delete_portfolio(username, portfolio_name):
    Portfolio.objects.filter(username=username, name=portfolio_name).delete()


def get_portfolios(username):

    try:

        ip_obj = Portfolio.objects.filter(username=username)
        print(f"{ip_obj=}")
        # t = serializers.serialize('json', ip_obj)
        # [print(i) for i in t]
        # print(t)
        return ip_obj

    except Portfolio.DoesNotExist:
        return False


def get_portfolios_with_locations(username):

    try:

        # portfolios = Portfolio.objects.filter(username=username)

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

