import datetime
import random
from pathlib import Path

import keycloak
import pandas as pd
import numpy as np

from src_django.api import common
from src_django.api import cryptography_wrapper
from src_django.api.controller import tmp_usr_model

cro_ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
       'ZIV0034703915', 'ZIV0034704013',
       'ZIV0034703953', 'ZIV0034703954')

esp_ids = ('CORRIDOR', 'MEETINGROOM', 'OFFICE1', 'OFFICE2',
        'OFFICE3', 'OFFICE4', 'OFFICE5')


def mock_token(username, password):
    if username == password == 'mirkofleks':
        return {'refresh_token': 'r3f75h',
                'access_token': 'ac355_70k3n',
                'expires_in': 300,
                'refresh_expires_in': 1800}
    if username == 'urbener_acc' and password == 'urbener':
        return {'refresh_token': 'chd4hshsh432',
                'access_token': 'sdf789789d_3',
                'expires_in': 300,
                'refresh_expires_in': 1800}
    if username == password == 'mytilineos':
        return {'refresh_token': 'n3k1t35k1t0k3n',
                'access_token': '15to_ac3ssdrug1',
                'expires_in': 300,
                'refresh_expires_in': 1800}
    else:
        raise keycloak.exceptions.KeycloakAuthenticationError(
            response_code=401)


def mock_userinfo(access_token):
    if access_token == 'ac355_70k3n':  # Asscess token for mirkofleks
        return {'sub': '5u8',
                'realm_access': {'roles': ['AGGREGATOR']},
                'preferred_username': 'mirkofleks'}
    if access_token == 'sdf789789d_3':  # Access token for urbener
        return {'sub': 'ag$qz57',
                'realm_access': {'roles': ['AGGREGATOR']},
                'preferred_username': 'urbener_acc'}
    if access_token == '15to_ac3ssdrug1':  # Access token for mytilineos
        return {'sub': 'random3r0j',
                'realm_access': {'roles': ['AGGREGATOR']},
                'preferred_username': 'mytilineos'}


def mock_req_building_by_usr_id(user_id):
    def mock_req_building_cro():
        buildings = []
        for i, b_id in enumerate(cro_ids):
            buildings.append({
                'building_id': b_id,
                'building_name': b_id,
                'address': f'Rade Koncara {i}',
                'latitude': (45.815399 + random.uniform(0.1, 0.9)),
                'longitude': (15.966568 + random.uniform(0.1, 0.9))})
        return {'type': 'buildings_by_user_id_response',
                'buildings': buildings}

    def mock_req_building_esp():
        buildings = []
        for i, b_id in enumerate(esp_ids):
            buildings.append({
                'building_id': b_id,
                'building_name': b_id,
                'address': f'Calle del Coso 34, Zaragoza',
                'latitude': (41.653421 + random.uniform(0.01, 0.04)),
                'longitude': (-0.883138 + random.uniform(0.01, 0.04))})
        return {'type': 'buildings_by_user_id_response',
                'buildings': buildings}

    username = tmp_usr_model.get_by_user_id(user_id=user_id)
    if username == 'mirkofleks':  # User id for mirkofleks
        return mock_req_building_cro()
    if username == 'urbener_acc' or username == 'mytilineos':  # User id for urbener_acc
        return mock_req_building_esp()


def mock_req_building_info(building_ids):
    return {'type': 'building_info_response',
            'buildings_info': mock_building_energy_list(building_ids)}


def mock_building_energy_list(building_ids=cro_ids):
    def mock_cro_buildings():
        koncar_df = pd.read_csv(Path(__file__).parent.resolve() / 
                    "active im en.csv", memory_map=True)
        data = koncar_df.to_dict()
        del data['Unnamed: 0']
        first = next(iter(data))
        timestamps = data[first]  # Keys are indexes and values are timestamps
        building_energy_list = []

        for k in timestamps.keys():
            ts = datetime.datetime.strptime(timestamps[k][:-4], "%Y-%m-%d %H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc).isoformat()
            timestamps[k] = ts

        del data['Timestamp']

        for k in data.keys():
            timeseries = []
            for i in timestamps.keys():
                timeseries.append({'timestamp': timestamps[i],
                                    'value': np.float64(data[k][i])})
            building_energy_list.append({'building_id': k,
                                            'energy_info': timeseries})
        building_energy_list = append_year(building_energy_list)
        return building_energy_list

    def mock_esp_buildings():
        urbener_df = pd.read_csv(Path(__file__).parent.resolve() / 
                    "BEYOND DATA URBENER.csv", memory_map=True)
        data = urbener_df.to_dict()
        del data['Unnamed: 0']
        first = next(iter(data))
        timestamps = data[first]  # Keys are indexes and values are timestamps
        building_energy_list = []

        for k in timestamps.keys():
            ts = datetime.datetime.strptime(timestamps[k][:-5], "%Y-%m-%dT%H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc).isoformat()
            timestamps[k] = ts

        del data['Timestamp']

        for k in data.keys():
            timeseries = []
            for i in timestamps.keys():
                timeseries.append({'timestamp': timestamps[i],
                                    'value': np.float64(data[k][i] * 1000.0)})
            building_energy_list.append({'building_id': k,
                                            'energy_info': timeseries})
        return building_energy_list

    if any(elem in cro_ids for elem in building_ids):
        return mock_cro_buildings()
    if any(elem in esp_ids for elem in building_ids):
        return mock_esp_buildings()


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
            'start_time': date.replace(hour=13 + i, minute=00, second=00, microsecond=0).isoformat(),
            'end_time': date.replace(hour=13 + 1 + i, minute=00, second=00, microsecond=0).isoformat(),
            'flexibility': random.uniform(100, 200)})
    return {'type': 'flexibility_demand_response',
            'demands': demands}


BEYOND_PRIVATE_PATH = Path(__file__).resolve().parent / 'priv.key'
BEYOND_PRIVATE_KEY_BYTES = cryptography_wrapper.load_private_key(
    BEYOND_PRIVATE_PATH)
BEYOND_PRIVATE_KEY = cryptography_wrapper.get_private_key_from_bytes(
    BEYOND_PRIVATE_KEY_BYTES)
