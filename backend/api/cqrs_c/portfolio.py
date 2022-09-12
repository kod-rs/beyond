from backend.api.model.portfolio import Portfolio
from backend.api.comm.constants import EXISTS,CREATED,NOT_EXISTS


def create_portfolio(username, portfolio_name, colour):
    print(username, portfolio_name, colour)

    if Portfolio.objects.filter(username=username, name=portfolio_name).exists():
        return {"status": False, "description": EXISTS}

    i = Portfolio.objects.create(
        username=username,
        name=portfolio_name,
        colour=colour
    )
    i.save()
    return {"status": True}

    # return {"status":bool(i)}
    # return True

def update_portfolio(username, current_name, params):
    if not Portfolio.objects.filter(username=username, name=current_name).exists():
        return {"status": False, "description": NOT_EXISTS}

    params = {k: v for k, v in params.items() if k in ["name", "colour"]}

    # return bool(
    Portfolio.objects \
        .filter(username=username, name=current_name) \
        .update(**params)
    # )
    return {"status": True}

def delete_portfolio(username, portfolio_name):
    if not Portfolio.objects.filter(username=username, name=portfolio_name).exists():
        return {"status": False, "description": NOT_EXISTS}

    Portfolio.objects.filter(username=username,
                             name=portfolio_name).delete()

    return  {"status": True,}
    # return bool(
    # )
