import json
import random
import requests

url = "http://localhost:8000/consumption"

def get_last():
    t = requests.get(
        f"{url}/{'portfolio_1'}/{'section_1'}/{'type_1'}/last",
        data={
            "section": "section_1",
            "type": "type_1",
            "portfolio": "portfolio_1",
            "options": "last"
        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def get_all():
    t = requests.get(
        f"{url}/{'portfolio_1'}/{'section_1'}/{'type_1'}",
        data={
            # "section": "section_1",
            # "type": "type_1",
            # "portfolio": "portfolio_1"
        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def post(colour,portfolio_name, section, _type):

    t = requests.post(
        f"{url}/{colour}",
        data={
            "portfolio": portfolio_name,
            "section": section,
            "type": _type,

            # "portfolio": portfolio
        },
        verify=False
    )

    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))



def main():
    post(str(4 * 2.3), "portfolio_1", "section_1", "type_1")

    # for i in range(10):
    #     post(str(i * 2.3), "portfolio_1", "section_1", "type_1")

    # get_all()
    get_last()

if __name__ == '__main__':
    main()