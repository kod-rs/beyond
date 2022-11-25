import datetime
import typing

from src_django.api.models import AggregatorFlexibility
from api import common

number_type = typing.Union[float, int]


def add(start_time: str,
        end_time: str,
        user_id: str,
        flexibility: number_type) -> bool:
    """
    Saves aggregator flexibility offer to a database

    Args:
        start_time: RFC 3339 string
        end_time: RFC 3339
        user_id: unique user id
        flexibility: amount of flexibility that can be offered

    Returns:
        True if saving was successful, False otherwise
    """
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
    """
    Reads data from the database based on user ID and requested period.

    Args:
        user_id: unique user id
        start_time: RFC 3339 string
        end_time: RFC 3339 string

    Returns:
        Either a list containing all the flexibilities matching the user and
        time or False in case of  no data found or error while reading data
    """
    try:
        start_time = common.datetime_from_rfc_string(start_time)
        end_time = common.datetime_from_rfc_string(end_time)
        flex_by_usr_id = AggregatorFlexibility.objects.filter(
            user_id=user_id,
            start_time__range=(start_time, end_time),
            end_time__range=(start_time + datetime.timedelta(hours=1),
                             end_time + datetime.timedelta(hours=1))
        ).values('start_time', 'end_time', 'flexibility')
        [d.update({'start_time': datetime.datetime.isoformat(d['start_time']),
                   'end_time': datetime.datetime.isoformat(d['end_time'])})
         for d in flex_by_usr_id]
        return list(flex_by_usr_id)
    except Exception as e:
        print(e)
        return False
