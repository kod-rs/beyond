import datetime
import random
from pathlib import Path

import keycloak
import pandas as pd

from src_django.api import common
from src_django.api import cryptography_wrapper

ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
       'ZIV0034703915', 'ZIV0034704013',
       'ZIV0034703953', 'ZIV0034703954')


def mock_token(username, password):
    if username == password == 'mirkofleks':
        return {'refresh_token': 'r3f75h',
                'access_token': 'ac355_70k3n'}
    else:
        raise keycloak.exceptions.KeycloakAuthenticationError(
            response_code=401)


def mock_userinfo(*_):
    return {'sub': '5u8',
            'realm_access': {'roles': ['AGGREGATOR']},
            'preferred_username': 'mirkofleks'}


def mock_req_building_by_usr_id(*_):
    buildings = []
    for i, b_id in enumerate(ids):
        buildings.append({
            'building_id': b_id,
            'building_name': f'building_name_{i}',
            'address': f'Rade Koncara {i}',
            'latitude': (45.815399
                         + random.uniform(0.1, 0.9)),
            'longitude': (15.966568
                          + random.uniform(0.1, 0.9))})
    return {'type': 'buildings_by_user_id_response',
            'buildings': buildings}


def mock_req_building_info(building_ids):
    return {'type': 'building_info_response',
            'buildings_info': mock_building_energy_list(building_ids)}


def mock_building_energy_list(building_ids=ids):
    df = pd.read_csv(Path(__file__).parent.resolve() / 'active im en.csv')
    rows = [df.iloc[index] for index in range(len(df))]
    building_energy_list = []
    for b_id in building_ids:
        timeseries = []
        for row in rows:
            ts = datetime.datetime.strptime(row['Timestamp'][:-4],
                                            "%Y-%m-%d %H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc).isoformat()
            timeseries.append({'timestamp': ts,
                               'value': row[b_id]})
        building_energy_list.append({'building_id': b_id,
                                     'energy_info': timeseries})
    building_energy_list = append_year(building_energy_list)
    return building_energy_list


def append_year(data):
    new_data = []
    _today = datetime.datetime.now()
    for building_info in data:
        new_energy = [{'timestamp': e['timestamp'].replace('2021', '2022'),
                       'value': e['value']}
                      for e in building_info['energy_info']
                      if (int(e['timestamp'][5:7]) <= _today.month
                      and int(e['timestamp'][8:10]) < _today.day)]
        new_data.append(
            {'building_id': building_info['building_id'],
             'energy_info': building_info['energy_info'] + new_energy})
    return new_data


def mock_get_flexibility_demand(date):
    date = common.datetime_from_rfc_string(date)
    demands = []
    for i in range(3):
        demands.append({
            'start_time': date.replace(hour=13 + i).isoformat(),
            'end_time': date.replace(hour=13 + 1 + i).isoformat(),
            'flexibility': random.uniform(100, 200)})
    return {'type': 'flexibility_demand_response',
            'demands': demands}


BEYOND_PRIVATE_PATH = Path(__file__).resolve().parent / 'priv.key'
BEYOND_PRIVATE_KEY_BYTES = cryptography_wrapper.load_private_key(
    BEYOND_PRIVATE_PATH)
BEYOND_PRIVATE_KEY = cryptography_wrapper.get_private_key_from_bytes(
    BEYOND_PRIVATE_KEY_BYTES)
