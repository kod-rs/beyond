from backend.api.model.location import Location


def get_all():
    return Location.objects.all().iterator()

