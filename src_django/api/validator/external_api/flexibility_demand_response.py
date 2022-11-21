from src_django.api.validator import common


def validate_flexibility_demand_response(data: dict) -> bool:
    """
    Validate "flexibility_demand_response" data from Beyond platform

    Args:
        data: data that should be formatted as specified in
            "flexibility_demand_response.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.external_api_dir /
                      'flexibility_demand_response.yaml')
    return common.validate(yaml_file_path, data)
