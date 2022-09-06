import json
from urllib.parse import unquote, parse_qs


def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))


def decode_data(payload):

    try:
        data_content = json.loads(payload.decode("utf-8"))
    except json.decoder.JSONDecodeError:
        data_content = unquote(payload)
        data_content = parse_qs(data_content)

    return data_content
