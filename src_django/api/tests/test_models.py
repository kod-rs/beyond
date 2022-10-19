from django.test import TestCase

from src_django.api.models import Data
from src_django.api.models import Location
from src_django.api.models import PersonPortfolio
from src_django.api.models import PortfolioLocation
from src_django.api.models.person import RoleChoices, Person
from src_django.api.tests import common


class LocationTestCase(TestCase):
    def setUp(self):
        common.set_up_locations()

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        assert loc1.longitude == 1.1
        assert loc1.latitude == 2.2

        assert loc2.longitude == 3.3
        assert loc2.latitude == 4.4


class DataTestCase(TestCase):
    def setUp(self):
        common.set_up_locations()
        common.set_up_data()

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        d1 = Data.objects.get(location=loc1)
        d2 = Data.objects.get(location=loc2)

        assert d1.value == 3.1
        assert d2.value == 3.2


class PersonTestCase(TestCase):
    def setUp(self):
        common.set_up_persons()

    def test_model_attrs(self):
        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)

        assert person1.role == RoleChoices.MANAGER.value
        assert person2.role == RoleChoices.AGGREGATOR.value


class PersonPortfolioTestCase(TestCase):
    def setUp(self):
        common.populate_database()

    def test_model_attrs(self):
        person1_portfolios = PersonPortfolio.objects.filter(person__id=1)

        assert len(person1_portfolios) == 2


class PortfolioTestCase(TestCase):
    def setUp(self):
        common.set_up_locations()
        common.set_up_portfolio()
        common.set_up_portfolio_location()

    def test_model_attrs(self):
        portfolio_location = PortfolioLocation.objects.filter(portfolio__id=1)

        assert len(list(portfolio_location)) == 2
