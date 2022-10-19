from datetime import datetime

from django.utils.timezone import make_aware

from src_django.api.models import Data
from src_django.api.models import Location
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
