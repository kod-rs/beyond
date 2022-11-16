from src_django.api.validator import common


def validate_algorithm_request(data: dict) -> bool:
    """
    Validate "algorithm_request" data from frontend
    Args:
        data: data that should be formatted as specified in
        "algorithm_request.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.internal_api_dir /
                      'algorithm_request.yaml')
    return common.validate(yaml_file_path, data)
