from pathlib import Path
import jsonschema
import yaml

schemas_dir = Path(__file__).resolve().parents[4] / 'schemas'
internal_api_dir = schemas_dir / 'internal_api'
beyond_flexopt_dir = schemas_dir / 'beyond_flexopt_api'


def validate(yaml_file_path, data):
    with open(yaml_file_path, 'r') as yaml_file:
        schema = yaml.safe_load(yaml_file)
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
