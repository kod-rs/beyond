import typing

from django.forms.models import model_to_dict

from src_django.api.models import Location
from src_django.api.models import PortfolioLocation


def get_for_portfolio(portfolio_id: int) -> typing.Union[list]:
    portfolio_location_relation = PortfolioLocation.objects.filter(
        portfolio__id=portfolio_id)
    location_ids = [p_l.location for p_l in portfolio_location_relation]
    location_ids = [model_to_dict(loc) for loc in location_ids]
    return location_ids


def get_by_location_id(location_id: str) -> typing.Union[dict, None]:
    location = Location.objects.filter(id=location_id)
    location = list(location.values())
    return location[0] if location else None


def get_by_location_ids(location_ids: typing.List[str]
                        ) -> typing.Union[typing.List[dict], None]:
    locations = []
    for location_id in location_ids:
        location = get_by_location_id(location_id)
        if location:
            locations.append(location)
    return locations if locations else None


def add_location(location_id: str, longitude: float, latitude: float) -> bool:
    try:
        new_location = Location(id=location_id,
                                longitude=longitude,
                                latitude=latitude)
        new_location.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True
