from src_django.api.validator import common


def validate_buildings_by_usr_id_resp(data: dict) -> bool:
    """
    Validate "buildings_by_user_id_response" data from Beyond platform
    Args:
        data: data that should be formatted as specified in
        "buildings_by_user_id_response.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.external_api_dir /
                      'buildings_by_user_id_response.yaml')
    return common.validate(yaml_file_path, data)


def validate_building_info(data: dict) -> bool:
    """
    Validate "building_info_response" data from Beyond platform
    Args:
        data: data that should be formatted as specified in
        "building_info_response.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.external_api_dir /
                      'building_info_response.yaml')
    return common.validate(yaml_file_path, data)
