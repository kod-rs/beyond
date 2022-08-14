import json
import pathlib


def join_with_curr_path(p):
    curr_path = pathlib.Path(__file__).parent.resolve()
    return curr_path / p


def _get_config(config_name):
    with open(join_with_curr_path(config_name)) as f:
        return json.loads(f.read())


role_validation_cfg = _get_config("role_validation.json")


def main():
    t = _get_config("role_validation.json")
    print(t)


if __name__ == '__main__':
    main()
