from backend.api.model.location import Location


def add(section, location_type, latitude, longitude):
    print(section, location_type, latitude, longitude)

    l = Location.objects.create(
        # device_id=device_id,
        section=section,
        type=location_type,
        latitude=latitude,
        longitude=longitude
    )

    l.save()


def delete(id):
    instance = Location.objects.get(id=id)
    instance.delete()
