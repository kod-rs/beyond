from src_django.api.validator import common


def validate_flexibility_demand_request(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'flexibility_demand_request.yaml')
    return common.validate(yaml_file_path, data)
