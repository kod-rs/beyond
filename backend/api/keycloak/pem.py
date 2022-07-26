import base64
import struct
import requests
import six
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from backend.api.keycloak.config import get_links
from backend.api.cqrs_c.pem_keys import add_keys


def base64_to_long(data):
    if isinstance(data, six.text_type):
        data = data.encode("ascii")

    decoded = base64.urlsafe_b64decode(bytes(data) + b'==')
    b = struct.unpack('%sB' % len(decoded), decoded)
    return int(''.join(["%02x" % byte for byte in b]), 16)


def generate_keys():
    url = get_links()["jwk-set-uri"]
    jwks = requests.get(url).json()
    pem_keys = {}

    for jwk in jwks['keys']:
        exponent = base64_to_long(jwk['e'])
        modulus = base64_to_long(jwk['n'])
        numbers = RSAPublicNumbers(exponent, modulus)
        public_key = numbers.public_key()
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        pem_keys[jwk["alg"]] = pem

    write_keys(pem_keys)


def write_keys(pem_keys):
    for k_type, k in pem_keys.items():
        add_keys(k_type, k)


def main():
    generate_keys()


if __name__ == '__main__':
    main()
