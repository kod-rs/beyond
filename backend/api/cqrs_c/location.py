from backend.api.model.location import Location
from backend.api.cqrs_q.portfolio import get_portfolio

def add(portfolio, section, location_type, latitude, longitude) -> bool:
    print(portfolio, section, location_type, latitude, longitude)

    # todo if portfolio does not exist create it,
    #  check if role is manager and how many portfolios exist

    p = get_portfolio(portfolio)

    try:
        l = Location.objects.create(
            portfolio=p,
            section=section,
            type=location_type,
            latitude=latitude,
            longitude=longitude
        )

        l.save()
        return True
    except Exception as e:
        print(e)
        return False


def delete(_id) -> bool:
    try:
        instance = Location.objects.get(id=_id)
        instance.delete()
        return True
    except Exception as e:
        print(e)
        return False
