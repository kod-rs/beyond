import ast
import json

from django.core import serializers

from backend.api.model.location import Location
from backend.api.cqrs_q.portfolio import get_portfolio


# def get_all():
#     t = serializers.serialize('json', Location.objects.all())
#     t = json.loads(t)
#     # print(t)
#
#     n = []
#     for i in t:
#         f = {}
#         p = i["pk"]
#         f["pk"] = p
#         f.update(i["fields"])
#         n.append(f)
#
#     t = n
#
#     try:
#         t = [{k: ast.literal_eval(v)[0] for k, v in i.items()} for i in t]
#     except ValueError:
#         try:
#             t = [{k: ast.literal_eval(v) for k, v in i.items()} for i in t]
#         except ValueError:
#             t = [{k: v for k, v in i.items()} for i in t]
#
#     return t

def get_user_portfolio(username, portfolio_name):
    # print("def get_user_portfolio(username, portfolio_name):")
    # portfolio = get_portfolio(portfolio_name)
    # print(f"{portfolio_name=}")

    locations = Location.objects.filter(portfolio__username=username, portfolio__name=portfolio_name)
    # print("locations", locations)
    # t = serializers.serialize('json', locations)
    # print(t)
    # print("---")
    # for i in t:
    #     print(i)
    return locations
    # return Portfolio.objects.filter(username=username)


def get_all_by_username(username):

    try:

        q = Location.objects.filter(portfolio__username=username)

    except Location.DoesNotExist:
        return False


    # print("q--------------------------")
    # print(f"{q=}")

    t = serializers.serialize('json', q)
    t = json.loads(t)
    # print(t)

    n = []
    for i in t:
        f = {}
        p = i["pk"]
        f["pk"] = p
        f.update(i["fields"])
        # del f["username"]
        n.append(f)

    t = n

    # fixme not safe
    try:
        t = [{k: ast.literal_eval(v)[0] for k, v in i.items()} for i in t]
    except ValueError:
        try:
            t = [{k: ast.literal_eval(v) for k, v in i.items()} for i in t]
        except ValueError:
            t = [{k: v for k, v in i.items()} for i in t]

    return t
