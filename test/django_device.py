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


def create_test_crud():

    url = "http://localhost:8000/testcrud/"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.put(url, headers=headers, data={
        "id": "ff",
        "newValue": "aaaa"
    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def get_test_crud():

    url = "http://localhost:8000/testcrud/"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, data={
    }, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # create()
    # get_one()
    # get()

    create_test_crud()
    # get_test_crud()

if __name__ == '__main__':
    main()
