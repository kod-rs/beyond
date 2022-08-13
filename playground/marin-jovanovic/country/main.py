import json


def extract_country_names():

    o = {}

    with open('countries.json') as json_file:
        data = json.load(json_file)

        f = data["features"]
        for i in f:
            r = i["properties"]["name"]
            o[r] = ""

        print(o)

        with open('out.json', 'w+', encoding='utf-8') as f:
            json.dump(o, f, ensure_ascii=False, indent=4)


def main():
    extract_country_names()


if __name__ == '__main__':
    main()
