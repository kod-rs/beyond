import json
import pathlib


def join_with_curr_path(p):
    curr_path = pathlib.Path(__file__).parent.resolve()
    return curr_path / p


def _get_config(config_name, curr_dir=True):
    if curr_dir:
        with open(join_with_curr_path(config_name)) as f:
            return json.loads(f.read())
    else:
        with open(config_name) as f:
            return json.loads(f.read())


vue_interface_path = pathlib.Path(__file__).parent.parent.parent.parent / "public" / "api_scheme" / "params.json"
role_validation_path = pathlib.Path(__file__).parent.parent / "role_action_validation" / "role_validation.json"

role_validation_cfg = _get_config(role_validation_path)
vue_interface_cfg = _get_config(vue_interface_path, curr_dir=False)

for route, actions in vue_interface_cfg.items():
    for a, k in actions.items():
        actions[a] = list(k)
