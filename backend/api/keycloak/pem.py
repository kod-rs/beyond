import base64
import json

import six
import struct

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.primitives import serialization
import requests
from decouple import config
import pathlib


def base64_to_long(data):
    if isinstance(data, six.text_type):
        data = data.encode("ascii")

    decoded = base64.urlsafe_b64decode(bytes(data) + b'==')
    b = struct.unpack('%sB' % len(decoded), decoded)
    return int(''.join(["%02x" % byte for byte in b]), 16)

def read_present_keys():
    current_folder = pathlib.Path(__file__).parent.resolve()

    key_types_path = current_folder / "key_types.json"

    present_keys = None
    if key_types_path.exists():
        with open(key_types_path, "r") as f:
            present_keys = json.loads(f.read())
            # print(present_keys)

    return present_keys




def generate_keys():

    url = config("KEYCLOAK_URL") + "certs"
    jwks = requests.get(url).json()
    pem_keys = {}

    current_folder = pathlib.Path(__file__).parent.resolve()

    key_types_path = current_folder / "key_types.txt"



    with open("key_types.txt", "w+") as f:

        for jwk in jwks['keys']:
            key_type = jwk["alg"]
            if (current_folder / f"{key_type}.key").exists():
                continue



            exponent = base64_to_long(jwk['e'])
            modulus = base64_to_long(jwk['n'])
            numbers = RSAPublicNumbers(exponent, modulus)
            public_key = numbers.public_key()
            pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            pem_keys[jwk["alg"]] = pem

        write_keys(pem_keys, current_folder)


def write_keys(pem_keys, current_folder):
    # current_folder = pathlib.Path(__file__).parent.resolve()

    key_types_path = current_folder / "key_types.json"

    with open(key_types_path, "w+") as f1:
        f1.write(json.dumps(pem_keys))

        for key_type, key in pem_keys.items():
            with open(current_folder / f"{key_type}.key", "wb+") as f:
                print(key)
                f.write(key)


def main():
    generate_keys()


if __name__ == '__main__':
    main()
    # read_present_keys()