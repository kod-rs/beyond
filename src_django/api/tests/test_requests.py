import sys

import requests


def main():
    data = {'location_ids': ['ZIV0034902130', 'ZIV0034902131']}

    response = requests.post('http://127.0.0.1:8000/location/',
                             json=data)
    breakpoint()
    pass


if __name__ == '__main__':
    sys.exit(main())
