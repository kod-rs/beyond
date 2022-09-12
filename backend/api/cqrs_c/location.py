from backend.api.model.location import Location
from backend.api.cqrs_q.portfolio import get_single_portfolio
from backend.api.model.portfolio import Portfolio


def update(username, portfolio, section, _type,
           params) -> bool:

    p = get_single_portfolio(username, portfolio)

    params = {k:v for k,v in params.items() if k in ["portfolio", "section", "type", "latitude", "longitude"]}
    if "portfolio" in params:
        print("switching portfolio")

        new_portfolio_name = params["portfolio"]
        t = Portfolio.objects.filter(username=username, name=new_portfolio_name).exists()
        if t:
            print("new target portfolio exists")
        else:
            print("new target portfolio not exists")
        target_portfolio_instance =      get_single_portfolio(username, new_portfolio_name)

        params["portfolio"] = target_portfolio_instance

    return bool(
        Location.objects \
            .filter(portfolio=p, section=section, type=_type) \
            .update(**params)
    )

def add(username, portfolio, section, location_type, latitude, longitude) -> str:
    print(portfolio, section, location_type, latitude, longitude)
    print(f"{username=} {portfolio=} {section=} {location_type=}")
    # todo if portfolio does not exist create it,
    #  check if role is manager and how many portfolios exist

    p = get_single_portfolio(username, portfolio)

    if p["exists"]:
        p = p["content"]

    e = Location.objects\
        .filter(portfolio=p, section=section, type=location_type).exists()

    if e:
        return "already exists for this portfolio, section, type"

    l = Location.objects.create(
        portfolio=p,
        section=section,
        type=location_type,
        latitude=latitude,
        longitude=longitude
    )

    l.save()
    return "created"


def delete(username, portfolio, section, _type) -> bool:
    p = get_single_portfolio(username, portfolio)
    instance = Location.objects.get(portfolio=p, section=section, type=_type)
    instance.delete()
    return True
