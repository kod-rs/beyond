import typing

from src_django.api.models import AggregatorFlexibility
from src_django.api.view import common

number_type = typing.Union[float, int]


def add(start_time: str,
        end_time: str,
        user_id: str,
        flexibility: number_type) -> bool:
    try:
        start_time = common.datetime_from_rfc_string(start_time)
        end_time = common.datetime_from_rfc_string(end_time)
        new_agr_flex = AggregatorFlexibility(user_id=user_id,
                                             start_time=start_time,
                                             end_time=end_time,
                                             flexibility=flexibility)
        new_agr_flex.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True


def get_for_portfolio(portfolio_id: int) -> typing.Union[list]:
    # portfolio_location_relation = PortfolioLocation.objects.filter(
    #     portfolio__id=portfolio_id)
    # location_ids = [p_l.location for p_l in portfolio_location_relation]
    # location_ids = [model_to_dict(loc) for loc in location_ids]
    # return location_ids
    return []


def get_by_location_id(location_id: str) -> typing.Union[dict, None]:
    # location = Location.objects.filter(id=location_id)
    # location = list(location.values())
    # return location[0] if location else None
    return {}
