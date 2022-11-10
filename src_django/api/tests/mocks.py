import datetime
from pathlib import Path

import keycloak
import pandas as pd
from src_django.api.view import common
import random


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


def mock_req_building_info(*_):
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


def mock_building_energy_list():
    ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
           'ZIV0034703915', 'ZIV0034704013',
           'ZIV0034703953', 'ZIV0034703954')
    df = pd.read_csv(Path(__file__).parent.resolve() / 'active im en.csv')
    rows = [df.iloc[index] for index in range(len(df))]
    building_energy_list = []
    for b_id in ids[:3]:
        timeseries = []
        for row in rows:
            ts = datetime.datetime.strptime(row['Timestamp'][:-4],
                                            "%Y-%m-%d %H:%M:%S")
            ts = ts.replace(tzinfo=datetime.timezone.utc).isoformat()
            timeseries.append({'timestamp': ts,
                               'value': row[b_id]})
        building_energy_list.append({'building_id': b_id,
                                     'energy_info': timeseries})
    return building_energy_list


def mock_get_flexibility_demand(_, date):
    date = common.datetime_from_rfc_string(date)
    demands = []
    for i in range(3):
        demands.append({
            'start_time': date.replace(hour=13 + i).isoformat(),
            'end_time': date.replace(hour=13 + 1 + i).isoformat(),
            'flexibility': random.uniform(100, 200)})
    return {'type': 'flexibility_demand_response',
            'demands': demands}
