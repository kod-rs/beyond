from backend.api.model.location import Location


def add(section, location_type, latitude, longitude) -> bool:
    print(section, location_type, latitude, longitude)

    try:
        l = Location.objects.create(
            # device_id=device_id,
            section=section,
            type=location_type,
            latitude=latitude,
            longitude=longitude)
        l.save()
        return True
    except Exception as e:
        print(e)
        return False


def delete(_id) -> bool:
    try:
        instance = Location.objects.get(id=_id)
        instance.delete()
        return True
    except Exception as e:
        print(e)
        return False
