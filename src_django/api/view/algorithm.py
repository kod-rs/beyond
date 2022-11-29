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
        req_flex = demand['flexibility_amount']
        interval = _dict_to_interval(demand['interval'])

        offered_flex, info = algorithm(
            building_energy_list=building_energy_list,
            interval=interval,
            flex_amount=demand['flexibility_amount'])

        yield {'offered_flexibility': offered_flex,
               'requested_flexibility': req_flex,
               'interval': _interval_to_strings(interval),
               'building_info': _building_infos_to_dict(info)}


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
        from_t=common.datetime_from_rfc_string(in_dict['from']),
        to_t=common.datetime_from_rfc_string(in_dict['to']))


def _interval_to_strings(interval: TimeInterval) -> dict:
    return {'from': interval.from_t.isoformat(),
            'to': interval.to_t.isoformat()}


def _building_infos_to_dict(in_list: typing.List[CurrentBuildingInfo]) -> list:
    ret = []
    for building in in_list:
        ret.append({
            'building_id': building.building_id,
            'interval': {
                'from': building.time_interval.from_t.isoformat(),
                'to': building.time_interval.to_t.isoformat()},
            'flexibility': building.flex})
    return ret
