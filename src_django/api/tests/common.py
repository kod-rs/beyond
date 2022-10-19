import random
from datetime import datetime, timedelta

from django.utils.timezone import make_aware

from src_django.api.models import Data
from src_django.api.models import Location
from src_django.api.models import PersonPortfolio
from src_django.api.models import Portfolio
from src_django.api.models import PortfolioLocation
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


def set_up_portfolio():
    Portfolio.objects.create(id=1, name='p1')
    Portfolio.objects.create(id=2, name='p2')


def set_up_portfolio_location():
    PortfolioLocation.objects.create(id=1,
                                     location=Location.objects.get(id='ABC1'),
                                     portfolio=Portfolio.objects.get(id=1))
    PortfolioLocation.objects.create(id=2,
                                     location=Location.objects.get(id='ABC2'),
                                     portfolio=Portfolio.objects.get(id=1))


def populate_database():
    for index in range(1, 11):
        # create locations
        Location.objects.create(id=f'Location-{index}',
                                longitude=index + index / 10,
                                latitude=index + index / 20)
        for i in range(1, 11):
            # create data for every location
            Data.objects.create(
                timestamp=make_aware(datetime.now() + timedelta(minutes=i)),
                value=random.randrange(10, 100),
                location=Location.objects.get(id=f'Location-{index}'))

    for index in range(1, 3):  # split 10 locations between two persons
        Person.objects.create(
            id=index,
            role=RoleChoices.values[random.randint(0, 1)])
        for i in range(1, 3):
            pp_id = index * 100 + i
            Portfolio.objects.create(id=pp_id,
                                     name=f'Portfolio{pp_id}')
            PersonPortfolio.objects.create(
                person=Person.objects.get(id=index),
                portfolio=Portfolio.objects.get(id=pp_id))

    # split locations into 4 groups
    locs = [list(Location.objects.all())[:3],
            list(Location.objects.all())[3:6],
            list(Location.objects.all())[6:9],
            list(Location.objects.all())[9:]]
    portfolios = list(Portfolio.objects.all())

    # give each portfolio part of the locations
    for locx, portfolio in zip(locs, portfolios):
        for location in locx:
            PortfolioLocation.objects.create(location=location,
                                             portfolio=portfolio)
