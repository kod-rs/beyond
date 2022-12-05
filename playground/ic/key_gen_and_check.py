import json
import os
import subprocess
import sys
from pathlib import Path


def generate_key_pair() -> (bytes, bytes):
    private_key_process = subprocess.Popen(['openssl', 'genrsa', '1024'],
                                           stdout=subprocess.PIPE)

    private_key = private_key_process.communicate()[0]

    public_key_process = subprocess.Popen(['openssl',
                                           'rsa',
                                           '-',
                                           '-outform',
                                           'PEM',
                                           '-pubout'],
                                          stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE)

    public_key = public_key_process.communicate(input=private_key)[0]

    return private_key, public_key


def save_keys(private_key: bytes,
              public_key: bytes,
              dir_name='keys') -> (Path, Path):
    parent_dir = Path(__file__).resolve().parent
    keys_dir = parent_dir / dir_name

    if not os.path.isdir(keys_dir):
        os.mkdir(keys_dir)

    private_key_file = keys_dir / 'priv.key'
    public_key_file = keys_dir / 'pub.key'

    with open(str(private_key_file), 'wb') as file:
        file.write(private_key)

    with open(str(public_key_file), 'wb') as file:
        file.write(public_key)

    return private_key_file, public_key_file


def hash_algorithm(private_key_path: Path, data: dict) -> bytes:
    hash_process = subprocess.Popen(['openssl',
                                     'dgst',
                                     '-sha256',
                                     '-sigopt',
                                     'rsa_padding_mode:pss',
                                     '-sign',
                                     f'{private_key_path}'],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)

    bytes_data = json.dumps(data).encode('utf-8')
    hash_data = hash_process.communicate(input=bytes_data)[0]
    return hash_data


def verify_signature(public_key_path: Path, signed_data: dict) -> bool:
    signature = signed_data['hash']
    del signed_data['hash']

    with open('sig.file', 'wb') as file:
        file.write(signature)
    verify_process = subprocess.Popen(['openssl',
                                       'dgst',
                                       '-sha256',
                                       '-sigopt',
                                       'rsa_padding_mode:pss',
                                       '-verify',
                                       f'{public_key_path}',
                                       '-signature',
                                       'sig.file'],
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)

    """echo argument1 argument2 argument3 |
     xargs -l bash -c 'echo this is first:$0 second:$1 third:$2'"""
    bytes_data = json.dumps(signed_data).encode('utf-8')
    verified = verify_process.communicate(input=bytes_data)[0]
    verified = verified.decode('utf-8')

    return 'Verified OK' in verified


def main():
    sender_public_key, sender_private_key = generate_key_pair()
    receiver_public_key, receiver_private_key = generate_key_pair()

    sender_pub_path, sender_priv_path = save_keys(sender_private_key,
                                                  sender_public_key,
                                                  'sender_keys')

    recv_pub_path, recv_priv_path = save_keys(receiver_private_key,
                                              receiver_public_key,
                                              'receiver_keys')

    data = {'a': 1}

    hash_data = hash_algorithm(sender_priv_path, data)

    signed_data = {**data, 'hash': hash_data}

    verified = verify_signature(sender_pub_path, signed_data)

    print(f'{verified = }')


if __name__ == '__main__':
    sys.exit(main())
