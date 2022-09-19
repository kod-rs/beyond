from backend.api.cqrs_c.portfolio_colour_adapter import add_colour_to_log
from backend.api.model.portfolio import Portfolio
from backend.api.comm.constants import EXISTS,CREATED,NOT_EXISTS
# from backend.api.cqrs_c.colour import add_colour_to_log

def create_portfolio(username, portfolio_name, colour=None):
    print(username, portfolio_name, colour)

    if Portfolio.objects.filter(username=username, name=portfolio_name).exists():
        return {"status": False, "description": EXISTS}

    i = Portfolio.objects.create(
        username=username,
        name=portfolio_name,
        # colour=colour
    )
    i.save()

    if colour:
        # todo log colour
        print("log colour")
        add_colour_to_log(username,portfolio_name,colour)

    return {"status": True}

    # return {"status":bool(i)}
    # return True

def update_portfolio(username, current_name, params):
    if not Portfolio.objects.filter(username=username, name=current_name).exists():
        return {"status": False, "description": NOT_EXISTS}

    portfolio_name = current_name
    if "name" in params:
        Portfolio.objects \
            .filter(username=username, name=current_name) \
            .update(name=params["name"])
            # .update(**params)

        portfolio_name = params["name"]

    if "colour" in params:
        r = add_colour_to_log(username, portfolio_name, params["colour"])
        return r

    # params = {k: v for k, v in params.items() if k in ["name", "colour"]}
    # return bool(
    # )
    #
    return {"status": True}

def delete_portfolio(username, portfolio_name):
    if not Portfolio.objects.filter(username=username, name=portfolio_name).exists():
        return {"status": False, "description": NOT_EXISTS}

    Portfolio.objects.filter(username=username,
                             name=portfolio_name).delete()

    return  {"status": True,}
    # return bool(
    # )
