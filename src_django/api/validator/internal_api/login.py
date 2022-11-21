from src_django.api.validator import common


def validate_internal_login(data: dict) -> bool:
    """
      Validate "login_request" data from frontend
      Args:
          data: data that should be formatted as specified in
          "login_request.yaml"

      Returns:
          True if the validation was successful, False otherwise

    """
    yaml_file_path = (common.internal_api_dir /
                      'login_request.yaml')
    return common.validate(yaml_file_path, data)
