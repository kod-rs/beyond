import typing

from src_django.api.models import BuildingFlexibility
from src_django.api.view import common

number_type = typing.Union[float, int]


def add(start_time: str,
        end_time: str,
        building_id: str,
        flexibility: number_type) -> bool:
    try:
        start_time = common.datetime_from_rfc_string(start_time)
        end_time = common.datetime_from_rfc_string(end_time)
        new_building_flex = BuildingFlexibility(building_id=building_id,
                                                start_time=start_time,
                                                end_time=end_time,
                                                flexibility=flexibility)
        new_building_flex.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True
