from backend.api.model.location import Location


def add(section, type, latitude, longitude):

    l = Location.objects.create(
        # device_id=device_id,
        section=section,
        type=type,
        latitude=latitude,
        longitude=longitude
    )

    l.save()
