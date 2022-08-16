from backend.api.model.device import Device


def create(data_id, device_type, consumption):
    d = Device.objects.create(data_id=data_id,
                              device_type=device_type,
                              consumption=consumption)
    d.save()
