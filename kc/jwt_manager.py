import json

import requests

def pretty_print_json(payload):
    print(json.dumps(payload, indent=4, sort_keys=True))


def get_jwt():

    url = "http://localhost:8080/realms/beyond/protocol/openid-connect/certs"
    data = {}

    res = requests.get(url, data=data, verify=False)

    res_text = json.loads(res.text)

    pretty_print_json(res_text)

    return res_text



def main():
    # print(get_jwt())

    encoded = {
        "keys": [
            {
                "kid": "vdaec4Br3ZnRFtZN-pimK9v1eGd3gL2MHu8rQ6M5SiE",
                "kty": "RSA",
                "alg": "RS256",
                "use": "sig",
                "n": "4OPCc_LDhU6ADQj7cEgRei4VUf4PZH8GYsxsR6RSdeKmDvZ48hCSEFiEgfc3FIfh-gC4r9PtKucc_nkRofrAKR4qL8KNNoSuzQAOC92Yz6r7Ao4HppHJ8-QVdo5H-d9wfNSlDLBSo5My4b4EnHb1HLuFxDqyhFpGvsoUJdgbt3m_Q3WAVb2yrM83S6HX__vrQvqUk2e7z5RNrI7LSsW3ZOz9fU7pvm8-kFFAIPJ7fOJIC7UQ9wBWg3YdwQ0B2b24jXjVr0QCGzqJ6o1G_UZYSJCDMGQDpDcEuYnvSKBLfVR-0EcAjolRhcSPjHlW0Cp0YU8qwWDHpjkbrMrFmxlO4Q",
                "e": "AQAB"
            }
        ]
    }
    import jwt



    t = jwt.decode(encoded, encoded["keys"][0]["n"], algorithms=["RS256"])
    print(t)

if __name__ == '__main__':
    main()