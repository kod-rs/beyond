import sys

import requests


def main():
    data = {'type': 'login_request',
            'username': 'mirkofleks',
            'password': 'mirkofleks'}

    response = requests.post('http://127.0.0.1:8000/login/',
                             json=data)
    response = response.json()
    breakpoint()
    pass


if __name__ == '__main__':
    sys.exit(main())
