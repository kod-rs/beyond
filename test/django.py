import json

import requests


def user_pass_f():

    url = "http://localhost:8000"
    headers = {
        "username": "user1",
        "password": "p"
    }

    t = requests.post(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_post_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.post(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_f():

    url = "http://localhost:8000"
    headers = {
        "username": "a",
        "password": "a"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))





def main():
    user_pass_f()
    user_pass_get_f()
    user_pass_post_c()
    user_pass_get_c()

if __name__ == '__main__':
    main()
