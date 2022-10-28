from src_django.api.validator import common


def validate_buildings_by_usr_id_req(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'buildings_by_user_id_request.yaml')
    return common.validate(yaml_file_path, data)


def validate_building_info_req(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'building_info_request.yaml')
    return common.validate(yaml_file_path, data)
