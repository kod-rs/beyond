import datetime
import json

import requests
from django.http import JsonResponse

from src_django.settings import BEYOND_CONFIG


def false_status(response_type: str, msg: str) -> JsonResponse:
    return JsonResponse({
        'type': response_type,
        'status': False,
        'message': msg})


def json_decode(request_body: bytes) -> dict:
    try:
        return json.loads(request_body)
    except Exception as e:
        print(f'Exception while decoding the body={e}')
        return {}


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

    def req_flex_demand(self, req_type, date):
        data = {'type': req_type,
                'date': date}
        # TODO remove mock
        # resp = self._send(data)
        # return resp
        return _get_flexibility_demand_mock(date)


# TODO delete all the mock data below
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


def _get_flexibility_demand_mock(date):
    import random
    date = datetime_from_rfc_string(date)
    demands = []
    for i in range(3):
        demands.append({
            'start_time': date.replace(hour=13 + i).isoformat(),
            'end_time': date.replace(hour=13 + 1 + i).isoformat(),
            'flexibility': random.uniform(100, 200)})
    return {'type': 'flexibility_demand_response',
            'demands': demands}


def datetime_from_rfc_string(rfc_string: str) -> datetime.datetime:
    dt = datetime.datetime.fromisoformat(rfc_string)
    return dt
