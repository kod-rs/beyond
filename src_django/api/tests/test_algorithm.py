import datetime

import pandas as pd
from django.test import TestCase

from src_django.api.flexopt_algorithm import algorithm
from src_django.api.flexopt_algorithm.main import BuildingEnergy
from src_django.api.flexopt_algorithm.main import EnergyInfo
from src_django.api.flexopt_algorithm.main import MONTHS
from src_django.api.flexopt_algorithm.main import TimeInterval
from pathlib import Path


class AlgorithmTestCase(TestCase):
    def setUp(self):
        pass

    def test_algorithm(self):
        # TODO don't read from CSV
        date_from = datetime.datetime(year=2022, month=4, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc)

        date_to = datetime.datetime(year=2022, month=4, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc)

        interval = TimeInterval(date_from, date_to)

        flex_amount = 303
        month = MONTHS[1]
        csv_file = Path(__file__).parent.resolve() / 'active im en.csv'
        df = pd.read_csv(csv_file)
        # df = df.drop(['Unnamed: 0'], axis=1).reset_index(drop=True)
        _ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030',
                'ZIV0034703915', 'ZIV0034704013',
                'ZIV0034703953', 'ZIV0034703954')
        rows = [df.iloc[index] for index in range(len(df))]
        building_ids = [b_id for b_id in df.keys()[2:]]

        building_energy = {
            b_id: [{'ts': datetime.datetime.strptime(row['Timestamp'][:-4],
                                                     "%Y-%m-%d %H:%M:%S"),
                    'value': row[b_id]}
                   for row in rows]
            for b_id in building_ids}

        building_energy = [BuildingEnergy(building_id=b_id,
                                          energy_info=[
                                              EnergyInfo(
                                                  timestamp=timeseries['ts'],
                                                  value=timeseries['value'])
                                              for timeseries in b_values])
                           for b_id, b_values in building_energy.items()]

        total_flex, building_info = algorithm(
            building_energy_list=building_energy,
            interval=interval,
            flex_amount=flex_amount,
            month=month)

        assert total_flex == flex_amount
        assert len(building_info) == 3
        assert building_info[0].flex == 130.0
