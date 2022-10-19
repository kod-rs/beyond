from django.utils import timezone

from playground.ic.backend_old.api.comm.constants import EXISTS, CREATED, NOT_EXISTS
from playground.ic.backend_old.api.cqrs_c.colour_history import update_or_create_colour_history
from playground.ic.backend_old.api.cqrs_q.portfolio import get_single_portfolio
from playground.ic.backend_old.api.model.portfoliocolouradapter import PortfolioColourAdapter


def is_portfolio_colour_entry_present(username, portfolio):
    if not PortfolioColourAdapter.objects.filter(portfolio__username=username,
                                                 portfolio__name=portfolio).exists():
        return False
    return True


def get_portfolio_colour_adapter(username, portfolio):
    print(f"{username=} {portfolio=}")
    if not PortfolioColourAdapter.objects.filter(portfolio__username=username,
                                                 portfolio__name=portfolio).exists():
        return NOT_EXISTS
    return PortfolioColourAdapter.objects.filter(portfolio__username=username,
                                                 portfolio__name=portfolio)


def clear_history(username, portfolio):
    get_portfolio_colour_adapter(username, portfolio).delete()


def get_last_colour(username, portfolio):
    if is_portfolio_colour_entry_present(username, portfolio):

        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp') \
            .first()

    else:
        print(f"portfolio-colour not present for {username=} {portfolio=}")
        return {"status": False}

    return {"status": True, "colour_timestamp": str(u.timestamp),
            "colour_hex": u.colour.colour}


def get_all_colours(username, portfolio):
    if is_portfolio_colour_entry_present(username, portfolio):
        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp')

        values = {str(i.timestamp): i.colour.colour for i in u}

        return {"status": True, "values": values, "order": "descending"}
    return {"status": False}


def delete_portfolio_colour_entries(username, portfolio):
    if is_portfolio_colour_entry_present(username, portfolio):
        get_portfolio_colour_adapter(username, portfolio) \
            .delete()
        return {"status": True}

    return {"status": False}


def add_color_to_log(username, portfolio, colour_hex):
    if str(colour_hex).startswith("#"):
        colour_hex = colour_hex[1:]

    max_log = 10

    # todo rewrite with this
    #     insert into api_user (id, portfolio, username, history_colour_id_id, timestamp_colour_change) select 14, 'a', 'a', 3, '2022-09-08 18:58:09.432646+02' where (select history_colour_id_id from api_user where username='a' and portfolio='a' order by timestamp_colour_change desc limit 1) != 4;

    # todo optimize using transaction

    portfolio_object = get_single_portfolio(username, portfolio)
    if portfolio_object["exists"]:
        portfolio_object = portfolio_object["content"]
    else:
        return {"err": "portfolio not exists", "status": False}

    colour_object = update_or_create_colour_history(colour_hex)

    if is_portfolio_colour_entry_present(username, portfolio):

        u = get_portfolio_colour_adapter(username, portfolio) \
            .order_by('-timestamp') \
            .first()

        if colour_object.id == u.colour:
            print("this is last entry in db, nothing is changed")
            return {"status": False, "description": EXISTS}

    delete_old_entry_with_same_value(colour_object, portfolio, username)

    create_portfolio_colour_adapter(colour_object, portfolio_object)

    count = get_history_log_count(portfolio, username)

    delete_old(count, max_log, portfolio, username)

    return {"status": True, "description": CREATED}


def delete_old_entry_with_same_value(colour_object, portfolio, username):
    if is_portfolio_colour_entry_present(username, portfolio):
        # remove current colour from log
        get_portfolio_colour_adapter(username, portfolio) \
            .filter(
            colour=colour_object.id
        ) \
            .delete()


def create_portfolio_colour_adapter(colour_object, portfolio_object):
    u = PortfolioColourAdapter.objects.create(
        portfolio=portfolio_object,
        colour=colour_object,
        timestamp=timezone.now()
    )
    u.save()


def get_history_log_count(portfolio, username):
    count = get_portfolio_colour_adapter(username, portfolio) \
        .values("colour") \
        .distinct() \
        .count()
    return count


def delete_old(count, max_log, portfolio, username):
    if count > max_log:
        get_portfolio_colour_adapter(username, portfolio) \
            .order_by('timestamp') \
            .first().delete()


