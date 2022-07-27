from backend.api.model.building import Building

# get_or_create
# update_or_create

def create(building_id, building_type, section, latitude, longitude):
    b = Building.objects.create(
        building_id=building_id,
        building_type=building_type,
        section=section,
        latitude=latitude,
        longitude=longitude
    )

    b.save()

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
