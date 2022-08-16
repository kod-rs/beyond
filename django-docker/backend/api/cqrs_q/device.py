from backend.api.model.device import Device


def get_all():
    return Device.objects.all().iterator()


def get_by_id(id):
    return Device.objects.filter(id=id)
