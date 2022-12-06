import json
import os
import sys
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


def save_keys(private_key: bytes,
              public_key: bytes,
              dir_name: Path = None) -> (Path, Path):
    """
    Save the byte formatted keys into a directory for later use.

    Args:
        private_key: Private key in byte format
        public_key: Public key in byte format
        dir_name: Directory where the keys will be saved. If it does not exist
            or is not defined, it will be created

    Returns:
            (private key path, public key path)
    """
    if not dir_name:
        dir_name = Path(__file__).resolve().parent / 'keys'
    if dir_name and not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    private_key_file = dir_name / 'priv.key'
    with open(str(private_key_file), 'wb') as file:
        file.write(private_key)

    public_key_file = dir_name / 'pub.key'
    with open(str(public_key_file), 'wb') as file:
        file.write(public_key)

    return private_key_file, public_key_file


def load_keys(private_key_path: Path, public_key_path: Path) -> (bytes, bytes):
    """
    Load the private and the public key defined by their respective paths.

    Args:
        private_key_path: Path to the file containing the private key
        public_key_path: Path to the file containing the public key

    Returns:
        (private key bytes, public key bytes)
    """
    return load_private_key(private_key_path), load_public_key(public_key_path)


def load_private_key(private_key_path: Path) -> bytes:
    """
    Load the private key defined by the path.

    Args:
        private_key_path: Path to the file containing the private key

    Returns:
        private key bytes
    """
    with open(str(private_key_path), 'rb') as file:
        private_key_bytes = file.read()

    return private_key_bytes


def load_public_key(public_key_path: Path) -> bytes:
    """
    Load the public key defined by the path.

    Args:
        public_key_path: Path to the file containing the public key

    Returns:
        public key bytes
    """
    with open(str(public_key_path), 'rb') as file:
        public_key_bytes = file.read()

    return public_key_bytes


def get_private_bytes(private_key: rsa.RSAPrivateKey) -> bytes:
    """
    Transform the rsa.PrivateKey into bytes

    Args:
        private_key: Object from which the bytes will be extracted

    Returns:
        Byte representation of the private key

    """
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())
    return private_key_bytes


def get_public_key_bytes(public_key: rsa.RSAPublicKey) -> bytes:
    """
    Transform the rsa.PublicKey into bytes

    Args:
        public_key: Object from which the bytes will be extracted

    Returns:
        Byte representation of the public key

    """
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return public_key_bytes


def get_private_key_from_bytes(private_key_bytes: bytes) -> rsa.RSAPrivateKey:
    """
    Get the rsa.RSAPrivateKey created from the input bytes
    Args:
        private_key_bytes: Byte representation of the private key

    Returns:
        rsa.RSAPrivateKey representation of the input bytes
    """
    private_key = serialization.load_pem_private_key(private_key_bytes,
                                                     password=None)
    return private_key


def get_public_key_from_bytes(public_key_bytes: bytes) -> rsa.RSAPublicKey:
    """
    Get the rsa.RSAPublicKey created from the input bytes
    Args:
        public_key_bytes: Byte representation of the public key

    Returns:
        rsa.RSAPublicKey representation of the input bytes
    """
    public_key = serialization.load_pem_public_key(public_key_bytes)
    return public_key


def generate_key_pair() -> (rsa.RSAPrivateKey, rsa.RSAPublicKey):
    """
    Generate the private key and the corresponding public key

    Returns:
        (private key, public key)
    """
    private_key = rsa.generate_private_key(public_exponent=65537,
                                           key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sign(private_key: rsa.RSAPrivateKey, data: dict) -> str:
    """
    Sign the data with the private key

    Args:
        private_key: Key used for signing
        data: Data to be signed (firstly utf-8 encoded)

    Returns:
        Signature
    """
    data = json.dumps(data).encode('utf-8')
    sig = private_key.sign(data,
                           padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                       salt_length=padding.PSS.MAX_LENGTH),
                           hashes.SHA256())

    sig = sig.hex()
    return sig


def verify_signature(public_key: rsa.RSAPublicKey, signed_data: dict) -> bool:
    """
    Verify the signature for the requested data

    Args:
        public_key: Public key used for data verification
        signed_data: Data that contains both the original message and the
            signature

    Returns:
        True if verification is successful, False otherwise

    """
    signature = signed_data['signature']
    signature = bytes.fromhex(signature)

    data = {k: v for k, v in signed_data.items() if k != 'signature'}
    message = json.dumps(data).encode('utf-8')

    try:
        public_key.verify(signature,
                          message,
                          padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                      salt_length=padding.PSS.MAX_LENGTH),
                          hashes.SHA256())
        return True
    except InvalidSignature:
        return False


def main():
    parent_dir = Path(__file__).resolve().parent

    sender_private_key, sender_public_key = generate_key_pair()

    save_keys(get_private_bytes(sender_private_key),
              get_public_key_bytes(sender_public_key),
              dir_name=parent_dir / 'beyond_keys')

    data = {'type': 'message_type', 'payload': 'message_payload...'}
    hash_data = sign(sender_private_key, data)
    signed_data = {**data, 'signature': hash_data}

    # As a receiver, try to verify the received message
    received = signed_data
    verified = verify_signature(sender_public_key, received)
    print(f'Verified = ', verified)


if __name__ == '__main__':
    sys.exit(main())
