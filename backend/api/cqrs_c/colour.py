from django.core.serializers import serialize
from django.utils import timezone

from backend.api.cqrs_q.portfolio import get_single_portfolio
from backend.api.model.colourHistory import ColourHistory
from backend.api.model.portfolio import Portfolio
from backend.api.model.portfoliocolouradapter import PortfolioColourAdapter
from backend.api.comm.constants import EXISTS, CREATED, NOT_EXISTS

def is_portfolio_colour_entry_present(username, portfolio):
    if not PortfolioColourAdapter.objects.filter(portfolio__username=username, portfolio__name=portfolio).exists():
        return False
    return True

def get_portfolio_colour_adapter(username, portfolio):
    print(f"{username=} {portfolio=}")
    if not PortfolioColourAdapter.objects.filter(portfolio__username=username, portfolio__name=portfolio).exists():
        return NOT_EXISTS
    # print(PortfolioColourAdapter.objects.filter(portfolio__username=username, portfolio__name=portfolio).query)
    # print(PortfolioColourAdapter.objects.filter(portfolio__username=username, portfolio__name=portfolio))
    return PortfolioColourAdapter.objects.filter(portfolio__username=username, portfolio__name=portfolio)


# def clear_history(username, portfolio):
#     get_portfolio_colour_adapter(username, portfolio).delete()

def get_last_colour(username, portfolio):

    if is_portfolio_colour_entry_present(username, portfolio):

        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp') \
            .first()
        # print(u.timestamp, u.colour.colour)
        # print(str(u.timestamp), u.colour.colour)

    else:
        print(f"portfolio-colour not present for {username=} {portfolio=}")
        return {"status": False}

    return {"status": True, "colour_timestamp": str(u.timestamp), "colour_hex": u.colour.colour }


from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder


def get_all_colours(username, portfolio):

    if is_portfolio_colour_entry_present(username, portfolio):

        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp')
            # .only("timestamp", "colour")

        # serialized_q = json.dumps(list(u), cls=DjangoJSONEncoder)
        # print(serialized_q)
        values = {str(i.timestamp): i.colour.colour for i in u}

        return {"status": True, "values": values, "order": "descending"}
    return {"status":False}



def delete_portfolio_colour_entries(username, portfolio):
    # print(f"{username=} {portfolio=}")
    # p = get_single_portfolio(username, portfolio)
    if is_portfolio_colour_entry_present(username, portfolio):

        get_portfolio_colour_adapter(username, portfolio) \
            .delete()
        return {"status": True}

    return {"status": False}


def add_colour_to_log(username, portfolio, colour_hex):
    if str(colour_hex).startswith("#"):
        colour_hex = colour_hex[1:]

    # print(f"{username=} {portfolio=} {colour_hex=}")
    max_log = 10

    # todo rewrite with this
    #     insert into api_user (id, portfolio, username, history_colour_id_id, timestamp_colour_change) select 14, 'a', 'a', 3, '2022-09-08 18:58:09.432646+02' where (select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1) != 4;

    # todo optimize using transaction

    p = get_single_portfolio(username, portfolio)
    if p["exists"]:
        p = p["content"]
    else:
        return {"err": "portfolio not exists", "status": False}

    ch, _ = ColourHistory.objects.update_or_create(
        colour=colour_hex,
        defaults={ "colour": colour_hex}
    )
    ch.save()

    # t =  PortfolioColourAdapter.objects\
    #     .filter(portfolio__username=username, portfolio__name=portfolio)
    # print(t)
    # return {"a": "b"}

    if is_portfolio_colour_entry_present(username, portfolio):
        # if get_portfolio_colour_adapter(username, portfolio).exists():

        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp') \
            .first()

        if ch.id == u.colour:
            print("this is last entry in db, nothing is changed")
            return {"status": False, "description" : EXISTS}

    # p = Portfolio.objects.

    if is_portfolio_colour_entry_present(username, portfolio):
        # remove current colour from log
        get_portfolio_colour_adapter(username, portfolio) \
            .filter(
                colour=ch.id
            ) \
            .delete()

    # PortfolioColourAdapter \
    #     .objects \
    #
    #     .filter(
    #     portfolio__username=username, portfolio__name=portfolio,
    #     colour=ch.id
    # ) \
    #     .delete()

    # try:


    # p = Portfolio.objects.get(username=username, name=portfolio)
    # except

    u = PortfolioColourAdapter.objects.create(
        portfolio=p,
        # portfolio__username=username,
        # portfolio__name=portfolio,
        colour=ch,
        timestamp=timezone.now()
    )
    u.save()

    # PortfolioColourAdapter \
    # .objects \
    # .filter(        portfolio__username=username, portfolio__name=portfolio)\
    # .filter(portfolio=portfolio, username=username) \

    count = get_portfolio_colour_adapter(username, portfolio)\
        .values("colour") \
        .distinct() \
        .count()

    if count > max_log:
            get_portfolio_colour_adapter(username, portfolio)\
            .order_by('timestamp') \
            .first().delete()

    return {"status": True,"description" :  CREATED}
