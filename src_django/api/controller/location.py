import typing

from src_django.api.models import Location


def get_location_by_location_id(location_id: str) -> typing.Union[dict, None]:
    location = Location.objects.filter(id=location_id)
    location = list(location.values())
    return location[0] if location else None


def get_locations_by_location_ids(location_ids: typing.List[str]
                                  ) -> typing.Union[typing.List[dict], None]:
    locations = []
    for location_id in location_ids:
        location = get_location_by_location_id(location_id)
        if location:
            locations.append(location)
    return locations if locations else None


def add_location(location_id: str, longitude: float, latitude: float) -> bool:
    try:
        new_location = Location(id=location_id,
                                longitude=longitude,
                                latitude=latitude)
        new_location.save()
    except Exception as e:
        print(f'error={e}')
        return False
    return True
