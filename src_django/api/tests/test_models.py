from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware

from src_django.api.models import Data
from src_django.api.models import Location
from src_django.api.models.person import RoleChoices, Person
from src_django.api.models import PersonLocation


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(id="ABC1", longitude=1.1, latitude=2.2)
        Location.objects.create(id="ABC2", longitude=3.3, latitude=4.4)

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        assert loc1.longitude == 1.1
        assert loc1.latitude == 2.2

        assert loc2.longitude == 3.3
        assert loc2.latitude == 4.4


class DataTestCase(TestCase):
    def setUp(self):
        Location.objects.create(id="ABC1", longitude=1.1, latitude=2.2)
        Location.objects.create(id="ABC2", longitude=3.3, latitude=4.4)
        Data.objects.create(id=1,
                            timestamp=make_aware(datetime.now()),
                            value=3.1,
                            location=Location.objects.get(id="ABC1"))
        Data.objects.create(id=2,
                            timestamp=make_aware(datetime.now()),
                            value=3.2,
                            location=Location.objects.get(id="ABC2"))

    def test_model_attrs(self):
        loc1 = Location.objects.get(id="ABC1")
        loc2 = Location.objects.get(id="ABC2")

        d1 = Data.objects.get(location=loc1)
        d2 = Data.objects.get(location=loc2)

        assert d1.value == 3.1
        assert d2.value == 3.2


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(id=1, role=RoleChoices.MANAGER)
        Person.objects.create(id=2, role=RoleChoices.AGGREGATOR)

    def test_model_attrs(self):
        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)

        assert person1.role == RoleChoices.MANAGER.value
        assert person2.role == RoleChoices.AGGREGATOR.value


class PersonLocationTestCase(TestCase):
    def setUp(self):
        Person.objects.create(id=1, role=RoleChoices.MANAGER)
        Person.objects.create(id=2, role=RoleChoices.AGGREGATOR)

        Location.objects.create(id="ABC1", longitude=1.1, latitude=2.2)
        Location.objects.create(id="ABC2", longitude=3.3, latitude=4.4)

        PersonLocation.objects.create(id=1,
                                      person=Person.objects.get(id=1),
                                      location=Location.objects.get(id="ABC1"))

        PersonLocation.objects.create(id=2,
                                      person=Person.objects.get(id=2),
                                      location=Location.objects.get(id="ABC2"))

    def test_model_attrs(self):
        pl1 = PersonLocation.objects.get(id=1)
        pl2 = PersonLocation.objects.get(id=2)

        assert pl1.person.id == 1
        assert pl1.location.id == 'ABC1'

        assert pl2.person.id == 2
        assert pl2.location.id == 'ABC2'
