import json
import random

import requests

def get_valid_credentials():
    headers = {
        "username": "c",
        "password": "c"
    }

    return headers

def get_all_locations():

    url = "http://localhost:8000/locations/"
    headers = get_valid_credentials()

    t = requests.get(url, headers=headers, data={

    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def create():
    url = "http://localhost:8000/locations/"
    headers = get_valid_credentials()

    t = requests.post(url, headers=headers, data={
        "portfolio": "a",
        "section": str(random.randint(1,10)),
        "type": str(random.randint(1,10)),
        "latitude": str(random.randint(1,10)),
        "longitude": str(random.randint(1,10))

    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def patch():
    url = "http://localhost:8000/location/a/4/2"
    # headers = get_valid_credentials()

    t = requests.patch(url, headers={

    }, data={
        "portfolio": "b",
        # "section": str(random.randint(1, 10)),
        # "type": str(random.randint(1, 10)),
        "latitude": 2,
        "longitude": 1111111
    }, verify=False)
    print(t)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def delete():
    url = "http://localhost:8000/location/a/7/7"
    # headers = get_valid_credentials()

    t = requests.delete(url, headers={

    }, data={

    }, verify=False)
    print(t)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # get_all_locations()
    # create()
    # delete()
    patch()

if __name__ == '__main__':
    main()