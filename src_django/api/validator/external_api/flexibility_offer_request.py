from src_django.api.validator import common


def validate_flex_offer_req_agr(data: dict) -> bool:
    """
    Validate "flexibility_offer_by_aggregator" data from Beyond platform

    Args:
        data: data that should be formatted as specified in
            "flexibility_offer_by_aggregator.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.external_api_dir /
                      'flexibility_offer_by_aggregator.yaml')
    return common.validate(yaml_file_path, data)


def validate_flex_offer_req_building(data: dict) -> bool:
    """
    Validate "flexibility_offer_by_building" data from Beyond platform

    Args:
        data: data that should be formatted as specified in
        "flexibility_offer_by_building.yaml"

    Returns:
        True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.external_api_dir /
                      'flexibility_offer_by_building.yaml')
    return common.validate(yaml_file_path, data)
