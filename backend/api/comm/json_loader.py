import json
import pathlib
import csv


def join_with_curr_path(p):
    curr_path = pathlib.Path(__file__).parent.resolve()
    return curr_path / p


def _get_config(config_name, curr_dir=True, json_or_csv=True):
    p = join_with_curr_path(config_name) if curr_dir else config_name

    if json_or_csv:
        with open(p) as f:
            return json.loads(f.read())

    else:
        with open(p, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',',
                       quotechar='|')

            return [i for i in csv_reader]


vue_interface_path = pathlib.Path(__file__).parent.parent.parent.parent / "public" / "api_scheme" / "params.json"
role_validation_path = pathlib.Path(__file__).parent.parent / "role_action_validation" / "role_validation.json"

role_validation_cfg = _get_config(role_validation_path)
vue_interface_cfg = _get_config(vue_interface_path, curr_dir=False)

for route, actions in vue_interface_cfg.items():
    for a, k in actions.items():
        actions[a] = list(k)

# colours_cfg = _get_config("../config/colours.csv", curr_dir=True, json_or_csv=False)
#
# c = {}
#
# for i in colours_cfg[:10]:
#     c[i[0]] = {"hex": i[1]}
# colours_cfg = c
