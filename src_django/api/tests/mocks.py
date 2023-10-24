import csv
from curses import raw
import datetime
import random
from pathlib import Path

import keycloak
import pandas as pd

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
                "BEYOND_MIRKOFLEKS_PROCESSED.csv", memory_map=True)
        data = koncar_df.to_dict()
        del data['Unnamed: 0']

        timestamps = data[next(iter(data))]
        del data['Timestamp']

        building_energy_list = []

        for building_idx in data.keys():
            energy_info = []
            for index in timestamps.keys():
                energy_info.append({'timestamp': timestamps[index],
                                    'value': float(data[building_idx][index])})
            
            building_energy_list.append({'building_id': building_idx,
                                            'energy_info': energy_info})
        
        building_energy_list = append_year(building_energy_list)
        return building_energy_list

    def mock_esp_buildings():
        koncar_df = pd.read_csv(Path(__file__).parent.resolve() / 
                "BEYOND_URBENER_PROCESSED.csv", memory_map=True)
        data = koncar_df.to_dict()
        del data['Unnamed: 0']

        timestamps = data[next(iter(data))]
        del data['Timestamp']

        building_energy_list = []

        for building_idx in data.keys():
            energy_info = []
            for index in timestamps.keys():
                energy_info.append({'timestamp': timestamps[index],
                                    'value': float(data[building_idx][index] * 1000.0)})
            
            building_energy_list.append({'building_id': building_idx,
                                            'energy_info': energy_info})

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
    demands_dict = {}  # Declare as dict to abuse constant lookup time
    hours = sorted(random.sample(range(7, 21), 3)) # Constant time complexity, O(1)

    with open(Path(__file__).parent.resolve() / "DEMAND_VOLUME_PROCESSED.csv", "r") as f:
        raw_data = csv.reader(f)
        next(raw_data, None)  # Remove header

        for timestamp, value in raw_data:
            demands_dict[timestamp] = value

    for hour in hours:
        start = date.replace(hour=hour, minute=00, second=00, microsecond=0).isoformat()
        flexibility = random.uniform(100, 200)
        try:
            flexibility = demands_dict[start]
        except KeyError:
            pass

        demands.append({
            'start_time': start,
            'end_time': date.replace(hour=hour + 1, minute=00, second=00, microsecond=0).isoformat(),
            'flexibility': flexibility})
    return {'type': 'flexibility_demand_response',
            'demands': demands}


BEYOND_PRIVATE_PATH = Path(__file__).resolve().parent / 'priv.key'
BEYOND_PRIVATE_KEY_BYTES = cryptography_wrapper.load_private_key(
    BEYOND_PRIVATE_PATH)
BEYOND_PRIVATE_KEY = cryptography_wrapper.get_private_key_from_bytes(
    BEYOND_PRIVATE_KEY_BYTES)
