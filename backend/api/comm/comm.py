import json
from urllib.parse import unquote,parse_qs


def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))


def decode_data(payload):
    try:
        data_content = json.loads(payload.decode("utf-8"))
    except json.decoder.JSONDecodeError:

        # print("---")

        # print(parse_qs(payload))
        # pr:int(payload.text)
        data_content = unquote(payload)
        data_content = parse_qs(data_content)
        # print(type(data_content))
        # import brotli
        # # decompressed = brotli.decompress(payload)
        # dict_ = json.loads(data_content)
        # print(dict_)

    print(80 * "-")
    print(data_content)

    return data_content
