from django.db import utils

from backend.api.model.portfolio import Portfolio


def create_portfolio(username, portfolio_name, colour):
    i = Portfolio.objects.create(
        username=username,
        name=portfolio_name,
        colour_tmp=colour
    )
    i.save()

def update(username, current_name, params):

    return Portfolio.objects\
        .filter(username=username, name=current_name)\
        .update(**params)

def update_portfolio_colour(username, current_name, new_colour):
    return Portfolio.objects\
        .filter(username=username, name=current_name) \
        .update(colour=new_colour)

def update_portfolio_name(username, current_name, new_name):
    print(f"{username=} {current_name=} {new_name=}")

    return Portfolio.objects\
        .filter(username=username, name=current_name) \
        .update(name=new_name)


def update_portfolio(username, current_name, new_name=None, new_colour=None):

    return Portfolio.objects\
        .filter(username=username, name=current_name)\
        .update(name=new_name, colour=new_colour)


def create_or_update(username, current_name, new_name, colour):

    print("create_or_update")

    print(f"if have {username=} {current_name=}")
    print(f"update this {new_name=} {colour=}")
    try:
        i, _ = Portfolio.objects.update_or_create(
            username=username, name=current_name,
            defaults={"name": new_name, "colour": colour}
        )
        print(i)
        i.save()

        # i, _ = Colour.objects.

        return True
    except utils.IntegrityError:
        print("integrity err")
        return False


def delete_portfolio(username, portfolio_name):
    Portfolio.objects.filter(username=username, name=portfolio_name).delete()
