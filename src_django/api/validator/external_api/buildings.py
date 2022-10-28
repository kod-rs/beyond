from src_django.api.validator import common


def validate_buildings_by_usr_id_resp(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'beyond_flexopt_api' /
                      'buildings_by_user_id_response.yaml')
    return common.validate(yaml_file_path, data)
