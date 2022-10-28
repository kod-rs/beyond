from src_django.api.validator import common


def validate_buildings_by_user_id_request(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'frontend_to_backend' /
                      'buildings_by_user_id_request.yaml')
    return common.validate(yaml_file_path, data)
