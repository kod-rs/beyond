import jsonschema
import yaml

from src_django.api.validator import common


def validate_internal_login(credentials: dict) -> bool:
    yaml_file_path = (common.internal_api_dir /
                      'frontend_to_backend' /
                      'login_request.yaml')

    with open(yaml_file_path, 'r') as yaml_file:
        schema = yaml.safe_load(yaml_file)
    try:
        jsonschema.validate(instance=credentials, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
