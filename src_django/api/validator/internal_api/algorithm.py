from src_django.api.validator import common


def validate_algorithm_request(credentials: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'algorithm_request.yaml')
    abc = common.validate(yaml_file_path, credentials)
    return abc
