from django.test import TestCase

from src_django.api.models import Location


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(location_id="ABC1",
                                longitude=1.1,
                                latitude=2.2)
        Location.objects.create(location_id="ABC2",
                                longitude=3.3,
                                latitude=4.4)

    def test_model_attrs(self):
        loc1 = Location.objects.get(location_id="ABC1")
        loc2 = Location.objects.get(location_id="ABC2")

        assert loc1.longitude == 1.1
        assert loc1.latitude == 2.2

        assert loc2.longitude == 3.3
        assert loc2.latitude == 4.4
