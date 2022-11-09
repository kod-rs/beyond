from src_django.api.validator import common


def validate_internal_login(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'login_request.yaml')
    return common.validate(yaml_file_path, data)
