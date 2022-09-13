import json
import random
import requests

url = "http://localhost:8000/portfolio/"


def get():

    t = requests.get(
        url
        # f"{url}{portfolio}",
        # data={
        # },
        # verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def post():

    t = requests.post(
        url + "portfolio_1",
        data={
            "colour": "clr1"
        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def patch():

    t = requests.patch(
        url + "d",
        data={
            "name": "d",
            "colour": "p"

        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def delete():

    t = requests.delete(
        url + "c",
        data={
        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))



    # url = "http://localhost:8000/location//7/7"
    # # headers = get_valid_credentials()
    #
    # t = requests.delete(url, headers={
    #
    # }, data={
    #
    # }, verify=False)
    # print(t)
    # print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def main():
    # get_all_locations()
    # create()
    # delete()
    # patch()
    # post()
    get()
    # post()

if __name__ == '__main__':
    main()