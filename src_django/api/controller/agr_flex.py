import datetime
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


def get_by_usr_and_time(user_id: str,
                        start_time: str,
                        end_time: str) -> typing.Union[list, bool]:
    try:
        start_time = common.datetime_from_rfc_string(start_time)
        end_time = common.datetime_from_rfc_string(end_time)
        flex_by_usr_id = AggregatorFlexibility.objects.filter(
            user_id=user_id,
            start_time__range=(start_time, end_time),
            end_time__range=(start_time + datetime.timedelta(hours=1),
                             end_time + datetime.timedelta(hours=1))
        ).values('start_time', 'end_time', 'flexibility')

        flex_iso = []
        for f in flex_by_usr_id:
            flex_iso.append({
                'flexibility': f['flexibility'],
                'start_time': datetime.datetime.isoformat(f['start_time']),
                'end_time': datetime.datetime.isoformat(f['end_time'])})
        return flex_iso
    except Exception as e:
        print(e)
        return False
