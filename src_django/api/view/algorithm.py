import datetime
import json
import typing

from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.flexopt_algorithm import BuildingEnergy
from src_django.api.flexopt_algorithm import CurrentBuildingInfo
from src_django.api.flexopt_algorithm import EnergyInfo
from src_django.api.flexopt_algorithm import MONTHS
from src_django.api.flexopt_algorithm import TimeInterval
from src_django.api.flexopt_algorithm import algorithm
from src_django.api.validator.internal_api.algorithm import \
    validate_algorithm_request
from src_django.api.view import common


class AlgorithmView(APIView):
    def __init__(self):
        super().__init__()
        self._request_type = 'algorithm_request'
        self._response_type = 'algorithm_response'

    def post(self, request) -> JsonResponse:
        request_body = common.json_decode(request.body)
        if not validate_algorithm_request(request_body):
            return common.false_status(msg='invalid request',
                                       response_type=self._response_type)

        building_energy_list = dict_to_building_energy_list(
            request_body['building_energy_list'])
        interval = dict_to_interval(request_body['interval'])

        total_flex, info = algorithm(
            building_energy_list=building_energy_list,
            interval=interval,
            flex_amount=request_body['flexibility_amount'])

        building_info = building_infos_to_dict(info)

        return JsonResponse({'type': self._response_type,
                             'status': True,
                             'offered_flexibility': total_flex,
                             'building_info': building_info})


def dict_to_building_energy_list(in_dict: dict) -> typing.List[BuildingEnergy]:
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


def dict_to_interval(in_dict: dict) -> TimeInterval:
    return TimeInterval(
        from_t=common.datetime_from_rfc_string(in_dict['from']),
        to_t=common.datetime_from_rfc_string(in_dict['to']))


def building_infos_to_dict(in_list: typing.List[CurrentBuildingInfo]) -> list:
    ret = []
    for building in in_list:
        ret.append({
            'building_id': building.building_id,
            'interval': {
                'from': building.time_interval.from_t.isoformat(),
                'to': building.time_interval.to_t.isoformat()},
            'flexibility': building.flex})
    return ret
