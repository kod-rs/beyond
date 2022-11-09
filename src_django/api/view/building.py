import typing

import requests
from django.http import JsonResponse
from rest_framework.views import APIView

from src_django.api.validator import internal_api, external_api
from src_django.api.view import common
from src_django.settings import BEYOND_CONFIG

number_type = typing.Union[int, float]


class BuildingView(APIView):
    def __init__(self):
        super().__init__()

        self._req_building_by_usr_id = 'buildings_by_user_id_request'
        self._resp_building_by_usr_id = 'buildings_by_user_id_response'

        self._req_building_info = 'building_info_request'
        self._resp_building_info = 'building_info_response'

        self._beyond = BeyondConnection()

    def post(self, request) -> JsonResponse:
        request = common.json_decode(request.body)
        request_type = request.get('type')

        if request_type == self._req_building_by_usr_id:
            return self._post_building_by_user_id(request)

        if request_type == self._req_building_info:
            return self._post_building_info(request)

        return common.false_status(response_type='invalid_request_response',
                                   msg='invalid request type')

    def _post_building_by_user_id(self, req: dict) -> JsonResponse:

        if not internal_api.buildings.validate_buildings_by_usr_id_req(req):
            return common.false_status(self._resp_building_by_usr_id,
                                       'invalid request')

        beyond_data = self._beyond.req_building_by_usr_id(req['type'],
                                                          req['user_id'])

        if not external_api.buildings.validate_buildings_by_usr_id_resp(
                beyond_data):
            return common.false_status(self._resp_building_by_usr_id,
                                       'request failed')

        return JsonResponse({'type': self._resp_building_by_usr_id,
                             'buildings': beyond_data.get('buildings')})

    def _post_building_info(self, request: dict) -> JsonResponse:
        if not internal_api.buildings.validate_building_info_req(request):
            return common.false_status(self._req_building_info,
                                       'invalid request')

        beyond_data = self._beyond.req_building_info(request['type'],
                                                     request['building_ids'])

        if not external_api.buildings.validate_building_info(beyond_data):
            return common.false_status(self._req_building_info,
                                       'invalid request')

        return JsonResponse({'type': self._resp_building_info,
                             'buildings_info': beyond_data['buildings_info']})


class BeyondConnection:
    def __init__(self):
        self._url = BEYOND_CONFIG['URL']

    def _send(self, data: dict) -> dict:
        response = requests.post(self._url, json=data)
        response_data = response.json()
        return response_data

    def req_building_by_usr_id(self, req_type: str, usr_id: int):
        data = {'type': req_type,
                'user_id': usr_id}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return _req_building_by_usr_id_mock()

    def req_building_info(self, req_type, building_ids):
        data = {'type': req_type,
                'building_ids': building_ids}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return _get_building_info_mock()


def _req_building_by_usr_id_mock():
    import random
    buildings = []
    for i in range(100):
        buildings.append({
            'building_id': f'b_{i}',
            'building_name': f'building_name_{i}',
            'address': f'Ilica {i}',
            'latitude': (45.815399
                         + random.uniform(0.000_001, 0.000_009)),
            'longitude': (15.966568
                          + random.uniform(0.000_001, 0.000_009))})
    return {'type': 'buildings_by_user_id_response',
            'buildings': buildings}


def _get_building_info_mock():
    from pathlib import Path
    import pandas as pd
    import datetime
    csv_file = (Path(__file__).resolve().parents[1]
                / 'tests'
                / 'active im en.csv')
    df = pd.read_csv(csv_file)
    # df = df.drop(['Unnamed: 0'], axis=1).reset_index(drop=True)
    ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
           'ZIV0034703915', 'ZIV0034704013',
           'ZIV0034703953', 'ZIV0034703954')
    rows = [df.iloc[index] for index in range(len(df))]
    # building_ids = [b_id for b_id in df.keys()[2:]]

    building_energy_list = []
    for b_id in ids[:3]:
        timeseries = []
        for row in rows:
            ts = datetime.datetime.strptime(row['Timestamp'][:-4],
                                            "%Y-%m-%d %H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc)
            ts = ts.isoformat()
            timeseries.append({'timestamp': ts,
                               'value': row[b_id]})
        building_energy_list.append({'building_id': b_id,
                                     'info': timeseries})

    return {'type': 'building_info_response',
            'buildings_info': building_energy_list}
