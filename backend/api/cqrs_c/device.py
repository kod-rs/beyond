from backend.api.model.device import Device


# get_or_create
# update_or_create

def create(data_id, device_type, consumption):
    d = Device.objects.create(
        # device_id=device_id,
        data_id=data_id,
        device_type=device_type,
        consumption=consumption
    )

    d.save()

# def update(device_id, data_id, device_type, consumption):

# def update(building_id, building_type, section, latitude, longitude):
#
#     b = Building.objects.get_or_create(
#         building_id=building_id, defaults={"counter": 0}
#     )
#
#     b = Building.objects.create(
#         building_id=building_id,
#         building_type=building_type,
#         section=section,
#         latitude=latitude,
#         longitude=longitude
#     )
#
#     b.save()
# )
#
# def auth_user(ip):
#
#     i, _ = IpCounter.objects.get_or_create(
#         ip=ip, defaults={"counter": 0}
#     )
#     i.save()
