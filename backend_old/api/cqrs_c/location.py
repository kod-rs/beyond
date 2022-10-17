from backend_old.api.model.location import Location
from backend_old.api.cqrs_q.portfolio import get_single_portfolio
from backend_old.api.model.portfolio import Portfolio


def update(username,  portfolio,name,
           params) -> bool:

    p = get_single_portfolio(username, portfolio)
    params = filter_params(params)

    handle_portfolio_param(params, username)

    return bool(
        Location.objects \
            .filter(name=name, portfolio=p) \
            .update(**params)
    )


def handle_portfolio_param(params, username):
    if "portfolio" in params:
        print("switching portfolio")

        new_portfolio_name = params["portfolio"]
        t = Portfolio.objects \
            .filter(username=username, name=new_portfolio_name).exists()
        if t:
            print("new target portfolio exists")
        else:
            print("new target portfolio not exists")
        target_portfolio_instance = get_single_portfolio(username,
                                                         new_portfolio_name)

        params["portfolio"] = target_portfolio_instance


def check_location_exists(username, portfolio_name, location_name):
    p = get_single_portfolio(username, portfolio_name)
    if p["exists"]:
        p = p["content"]
    return Location.objects.filter(portfolio=p, name=location_name).exists()



def add(username, portfolio_name, location_name, params) -> str:
    # todo if portfolio does not exist create it,
    #  check if role is manager and how many portfolios exist

    print(username, portfolio_name, location_name, params)

    p = get_single_portfolio(username, portfolio_name)

    if p["exists"]:
        p = p["content"]

    if check_location_exists(username, portfolio_name, location_name):
        return "already exists for this portfolio, section, type"

    params = filter_params(params)

    if "name" in params:
        del params["name"]
    if "portfolio" in params:
        del params["portfolio"]

    l = Location.objects.create(
        portfolio=p,
        name=location_name,
        **params
    )

    l.save()
    return "created"


def filter_params(params):
    # params = {k:v for k,v in params.items() if k in ["name", "portfolio", "section", "type", "latitude", "longitude"]}


    params = {k: v for k, v in
              params.items() if k in ["section", "name", "portfolio",
                                      "type", "latitude", "longitude"]}
    return params


def delete(username, portfolio, name) -> bool:
    p = get_single_portfolio(username, portfolio)
    if p["exists"]:
        p = p["content"]
    else:
        return False
    try:
        instance = Location.objects.get(portfolio=p, name=name)
        instance.delete()
        return True
    except Location.DoesNotExist:
        return False
