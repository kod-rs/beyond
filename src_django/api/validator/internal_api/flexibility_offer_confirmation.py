from src_django.api.validator import common


def validate_flexibility_offer_confirmation(data: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'flexibility_offer_confirmation.yaml')
    return common.validate(yaml_file_path, data)
