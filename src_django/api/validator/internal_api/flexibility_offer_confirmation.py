from src_django.api.validator import common


def validate_flexibility_offer_confirmation(data: dict) -> bool:
    """
      Validate "flexibility_offer_confirmation_request" data from frontend

      Args:
          data: data that should be formatted as specified in
            "flexibility_offer_confirmation.yaml"

      Returns:
          True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.internal_api_dir /
                      'flexibility_offer_confirmation.yaml')
    return common.validate(yaml_file_path, data)
