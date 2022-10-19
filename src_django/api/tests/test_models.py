from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware

from src_django.api.models import Data
from src_django.api.models import Location
from src_django.api.models import ManagerAggregator
from src_django.api.models import PersonLocation
from src_django.api.models.person import RoleChoices, Person


def set_up_locations():
    Location.objects.create(id="ABC1", longitude=1.1, latitude=2.2)
    Location.objects.create(id="ABC2", longitude=3.3, latitude=4.4)


def set_up_data():
    Data.objects.create(id=1,
                        timestamp=make_aware(datetime.now()),
                        value=3.1,
                        location=Location.objects.get(id="ABC1"))
    Data.objects.create(id=2,
                        timestamp=make_aware(datetime.now()),
                        value=3.2,
                        location=Location.objects.get(id="ABC2"))


def set_up_persons():
    Person.objects.create(id=1, role=RoleChoices.MANAGER)
    Person.objects.create(id=2, role=RoleChoices.AGGREGATOR)


def set_up_person_location():
    PersonLocation.objects.create(id=1,
                                  person=Person.objects.get(id=1),
                                  location=Location.objects.get(id="ABC1"))

    PersonLocation.objects.create(id=2,
                                  person=Person.objects.get(id=2),
                                  location=Location.objects.get(id="ABC2"))


class LocationTestCase(TestCase):
    def setUp(self):
        set_up_locations()

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        assert loc1.longitude == 1.1
        assert loc1.latitude == 2.2

        assert loc2.longitude == 3.3
        assert loc2.latitude == 4.4


class DataTestCase(TestCase):
    def setUp(self):
        set_up_locations()
        set_up_data()

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        d1 = Data.objects.get(location=loc1)
        d2 = Data.objects.get(location=loc2)

        assert d1.value == 3.1
        assert d2.value == 3.2


class PersonTestCase(TestCase):
    def setUp(self):
        set_up_persons()

    def test_model_attrs(self):
        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)

        assert person1.role == RoleChoices.MANAGER.value
        assert person2.role == RoleChoices.AGGREGATOR.value


class PersonLocationTestCase(TestCase):
    def setUp(self):
        set_up_persons()
        set_up_locations()
        set_up_person_location()

    def test_model_attrs(self):
        pl1 = PersonLocation.objects.get(id=1)
        pl2 = PersonLocation.objects.get(id=2)

        assert pl1.person.id == 1
        assert pl1.location.id == 'ABC1'

        assert pl2.person.id == 2
        assert pl2.location.id == 'ABC2'


#
class ManagerAggregatorTestCase(TestCase):
    def setUp(self):
        set_up_persons()

        ManagerAggregator.objects.create(id=1,
                                         manager=Person.objects.get(id=1),
                                         aggregator=Person.objects.get(id=2))

        try:
            ManagerAggregator.objects.create(
                id=2,
                manager=Person.objects.get(id=2),
                aggregator=Person.objects.get(id=1))
        except ValueError as e:
            assert 'field must have a person that is a' in str(e)

    def test_model_attrs(self):
        manager = Person.objects.get(id=1)
        aggregator = Person.objects.get(id=2)

        manager_aggregator = ManagerAggregator.objects.get(id=1)
        manager_from_relation = manager_aggregator.manager
        aggregator_from_relation = manager_aggregator.aggregator

        assert manager.id == manager_from_relation.id
        assert manager.role == manager_from_relation.role

        assert aggregator.id == aggregator_from_relation.id
        assert aggregator.role == aggregator_from_relation.role
