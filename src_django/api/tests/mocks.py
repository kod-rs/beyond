import csv
import datetime
import random
from pathlib import Path

import keycloak

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
    def read_data_dict(filename):
        columns = []

        with open(Path(__file__).parent.resolve() / filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                row.pop(0)  # Remove unnecesarry first column
                if columns:
                    for i, value in enumerate(row):
                        columns[i].append(value)
                else:  # Handle the first row by initializing columns
                    columns = [[value] for value in row]
        # Convert the data into a column-major 2D array
        data_as_dict = {c[0]: c[1:] for c in columns}
        return data_as_dict

    def process_building_data(data, building_ids, conversion_factor=1.0):
        building_energy_list = []
        # Extract building names from the keys
        buildings = list(data.keys())[1:]
        valid_buildings = [b for b in buildings if b in building_ids]

        for building in valid_buildings:
            energy_info = []
            for i, value in enumerate(data[building]):
                energy_info.append({'timestamp': data['Timestamp'][i],
                                    'value': float(value) * conversion_factor})
            building_energy_list.append(
                {'building_id': building, 'energy_info': energy_info})

        return building_energy_list

    if any(elem in cro_ids for elem in building_ids):
        # Read and process data for 'cro_ids' buildings
        cro_buildings = read_data_dict("BEYOND_MIRKOFLEKS_PROCESSED.csv")
        building_energy_list = process_building_data(
            cro_buildings, building_ids)
        return append_year(building_energy_list)

    if any(elem in esp_ids for elem in building_ids):
        # Read and process data for 'esp_ids' buildings with a
        # conversion factor of 1000.0
        esp_buildings = read_data_dict("BEYOND_URBENER_PROCESSED.csv")
        building_energy_list = process_building_data(
            esp_buildings, building_ids, conversion_factor=1000.0)
        return building_energy_list


def append_year(data):
    new_building_energy_list = []
    # Get the current date and time
    today = datetime.datetime.now()

    for building_info in data:
        new_energy_info = []

        for energy_info in building_info['energy_info']:
            timestamp = energy_info['timestamp']
            year = timestamp[:4]  # Extract the year from the timestamp
            month = int(timestamp[5:7])  # Extract the month from the timestamp
            day = int(timestamp[8:10])  # Extract the day from the timestamp

            # Check if the timestamp is from the year 2021 and earlier than the current date
            if year == '2021' and (month < today.month or (month == today.month and day < today.day)):
                new_energy_info.append({
                    'timestamp': timestamp.replace('2021', '2022'),
                    'value': energy_info['value']
                })

        new_building_energy_list.append({
            'building_id': building_info['building_id'],
            'energy_info': building_info['energy_info'] + new_energy_info
        })

    return new_building_energy_list


def mock_get_flexibility_demand(date):
    # Convert the input date to a datetime object
    input_date = common.datetime_from_rfc_string(date)
    last_year = datetime.datetime.now() - datetime.timedelta(days=364)

    # Generate a list of 3 random hours between 7 and 20, O(1) time complexity
    hours = []
    start = 7
    for _ in range(4):
        hour = random.choice(range(start, start + 4))
        start += 4
        hours.append(hour)

    demands = []
    demands_dict = {}

    # Read demand data from a CSV file
    filepath = Path(__file__).parent.resolve() / "DEMAND_VOLUME_PROCESSED.csv"

    with open(filepath, "r") as f:
        raw_data = csv.reader(f)
        next(raw_data, None)  # Skip the header row

        for timestamp, value in raw_data:
            demands_dict[timestamp] = float(value)

    # Generate flexibility demands for the selected hours
    for hour in hours:
        start_time = last_year.replace(
            hour=hour, minute=0, second=0,
            microsecond=0, tzinfo=datetime.timezone.utc).isoformat()

        if start_time not in demands_dict:
            flexibility = random.uniform(100, 200)
        else:
            flexibility = demands_dict[start_time]

        start_time = input_date.replace(
            hour=hour, minute=0, second=0, microsecond=0).isoformat()
        end_time = input_date.replace(
            hour=hour + 1, minute=0, second=0, microsecond=0).isoformat()

        demands.append({
            'start_time': start_time,
            'end_time': end_time,
            'flexibility': flexibility
        })

    response = {
        'type': 'flexibility_demand_response',
        'demands': demands
    }

    return response


BEYOND_PRIVATE_PATH = Path(__file__).resolve().parent / 'priv.key'
BEYOND_PRIVATE_KEY_BYTES = cryptography_wrapper.load_private_key(
    BEYOND_PRIVATE_PATH)
BEYOND_PRIVATE_KEY = cryptography_wrapper.get_private_key_from_bytes(
    BEYOND_PRIVATE_KEY_BYTES)
