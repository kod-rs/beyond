from src_django.api.validator import common


def validate_flexibility_demand_response(credentials: dict) -> bool:
    yaml_file_path = (common.external_api_dir /
                      'flexibility_demand_response.yaml')
    return common.validate(yaml_file_path, credentials)
