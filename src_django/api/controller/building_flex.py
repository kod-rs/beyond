import datetime
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


def get_by_building_and_time(building_id: str,
                             start_time: str,
                             end_time: str) -> typing.Union[list, bool]:
    try:
        start_time = common.datetime_from_rfc_string(start_time)
        end_time = common.datetime_from_rfc_string(end_time)
        flex_by_building_id = BuildingFlexibility.objects.filter(
            building_id=building_id,
            start_time__range=(start_time, end_time),
            end_time__range=(start_time + datetime.timedelta(hours=1),
                             end_time + datetime.timedelta(hours=1))
        ).values('start_time', 'end_time', 'flexibility')
        [d.update({'start_time': datetime.datetime.isoformat(d['start_time']),
                   'end_time': datetime.datetime.isoformat(d['end_time'])})
         for d in flex_by_building_id]
        return list(flex_by_building_id)
    except Exception as e:
        print(e)
        return False
