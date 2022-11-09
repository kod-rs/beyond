from src_django.api.validator import common


def validate_algorithm_request(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'algorithm_request.yaml')
    return common.validate(yaml_file_path, data)
