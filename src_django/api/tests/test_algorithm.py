import datetime

from django.test import TestCase

from src_django.api.flexopt_algorithm import algorithm
from src_django.api.flexopt_algorithm.main import BuildingEnergy
from src_django.api.flexopt_algorithm.main import EnergyInfo
from src_django.api.flexopt_algorithm.main import TimeInterval
from src_django.api.tests import mocks


class AlgorithmTestCase(TestCase):
    def test_algorithm(self):
        date_from = datetime.datetime(year=2022, month=2, day=10, hour=9)
        date_from = date_from.replace(tzinfo=datetime.timezone.utc)
        date_to = datetime.datetime(year=2022, month=2, day=10, hour=12)
        date_to = date_to.replace(tzinfo=datetime.timezone.utc)
        interval = TimeInterval(date_from, date_to)
        flex_amount = 303
        ids = mocks.cro_ids
        building_energy = mocks.mock_building_energy_list(ids)
        building_energy = [BuildingEnergy(building_id=b['building_id'],
                                          energy_info=[EnergyInfo(
                                              timestamp=e['timestamp'],
                                              value=e['value'])
                                              for e in b['energy_info']])
                           for b in building_energy]

        total_flex, building_info = algorithm(
            building_energy_list=building_energy,
            interval=interval,
            flex_amount=flex_amount)

        assert total_flex == flex_amount
        assert len(building_info) == 3
        assert building_info[0].flex == 172.5


