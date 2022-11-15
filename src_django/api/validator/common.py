from pathlib import Path

import jsonschema
import yaml

schemas_dir = Path(__file__).resolve().parents[3] / 'schemas'
internal_api_dir = schemas_dir / 'internal_api'
external_api_dir = schemas_dir / 'external_api'


def validate(yaml_file_path, data):
    with open(yaml_file_path, 'r') as yaml_file:
        schema = yaml.safe_load(yaml_file)
    try:
        jsonschema.validate(instance=data, schema=schema,
                            format_checker=jsonschema.FormatChecker())
    except jsonschema.exceptions.ValidationError as e:
        print(f'VALIDATION FAILED={e}')
        return False
    return True
