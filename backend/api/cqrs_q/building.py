from backend.api.model.building import Building


def get_all():
    return Building.objects.all().iterator()
