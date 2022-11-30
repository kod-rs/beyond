import datetime
import typing

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api import common
from src_django.api.flexopt_algorithm import BuildingEnergy
from src_django.api.flexopt_algorithm import CurrentBuildingInfo
from src_django.api.flexopt_algorithm import EnergyInfo
from src_django.api.flexopt_algorithm import TimeInterval
from src_django.api.flexopt_algorithm import algorithm
from src_django.api.validator.internal_api.algorithm import \
    validate_algorithm_request


class AlgorithmView(APIView):
    """
    API for /algorithm
    """

    def __init__(self):
        super().__init__()
        self._request_type = 'algorithm_request'
        self._response_type = 'algorithm_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)
        if not validate_algorithm_request(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        offers = list(_get_algorithm_offers(request_body))

        return JsonResponse({'type': self._response_type,
                             'status': True,
                             'offers': offers})


def _get_algorithm_offers(request_body):
    demands = request_body['flexibility_demands']
    building_energy_list = _dict_to_building_energy_list(
        request_body['building_energy_list'])

    for demand in demands:
        offered_flex, info = algorithm(
            building_energy_list=building_energy_list,
            interval=_dict_to_interval(demand),
            flex_amount=demand['flexibility'])

        yield {'offered_flexibility': offered_flex,
               'requested_flexibility': demand['flexibility'],
               'start_time': demand['start_time'],
               'end_time': demand['end_time'],
               'building_info': list(_building_infos_to_dict(info))}


def _dict_to_building_energy_list(in_dict: dict
                                  ) -> typing.List[BuildingEnergy]:
    building_energy_list = []
    for building in in_dict:
        energy_info = []
        for energy in building['energy_info']:
            energy_info.append(EnergyInfo(
                timestamp=datetime.datetime.fromisoformat(energy['timestamp']),
                value=energy['value']))
        building_energy_list.append(
            BuildingEnergy(building_id=building['building_id'],
                           energy_info=energy_info))
    return building_energy_list


def _dict_to_interval(in_dict: dict) -> TimeInterval:
    return TimeInterval(
        from_t=common.datetime_from_rfc_string(in_dict['start_time']),
        to_t=common.datetime_from_rfc_string(in_dict['end_time']))


def _building_infos_to_dict(
        in_list: typing.List[CurrentBuildingInfo]) -> list:
    for building in in_list:
        yield {'building_id': building.building_id,
               'start_time': building.time_interval.from_t.isoformat(),
               'end_time': building.time_interval.to_t.isoformat(),
               'flexibility': building.flex}
