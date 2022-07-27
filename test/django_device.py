import json

import requests


def create():

    url = "http://localhost:8000/device/"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.post(url, headers=headers, data={
        "data_id": 1,
        "device_type": 1,
        "consumption": 1
    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def get_one():

    url = "http://localhost:8000/device/1"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, data={
    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def get():

    url = "http://localhost:8000/device"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, data={
    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # create()
    get_one()
    get()

if __name__ == '__main__':
    main()
