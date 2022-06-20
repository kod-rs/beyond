import json

import requests


def main():
    url = 'http://127.0.0.1:8000/login/'
    data = {
        "username": "Tracey_Ramos",
        "password": "c"
    }

    t = requests.post(url, data=data, verify=False)

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
