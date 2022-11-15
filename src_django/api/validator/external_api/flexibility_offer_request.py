from src_django.api.validator import common


def validate_flex_offer_req_agr(data: dict) -> bool:
    yaml_file_path = (common.external_api_dir /
                      'flexibility_offer_by_aggregator.yaml')
    return common.validate(yaml_file_path, data)


def validate_flex_offer_req_building(data: dict) -> bool:
    yaml_file_path = (common.external_api_dir /
                      'flexibility_offer_by_building.yaml')
    return common.validate(yaml_file_path, data)
