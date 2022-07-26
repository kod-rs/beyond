import json


def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))
