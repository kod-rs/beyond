import json


def bytes_to_json(content):
    return json.loads(content.decode("utf-8"))

import re

from django.urls.converters import DEFAULT_CONVERTERS

# request_body=b'{"portfolio":"a","type":"a","section":"a","latitude":47.989921667414166,"longitude":-101.6015625,"synchronizer_token":"0c6e313ff72e2e8bde54f0661a3e5d3feb1f8524753ec4738467db73dd838c9bf56fc7ca0ccd54f1dff6d9ba669d98f8c8e34ea286d1d6ab1ca25f8f62bbbf93a54f2d25decc333d565b9b2e11d2ebb59fc687a20adc28a3e6fe9fa7609270247b16fce2052349ca2a1d5433ce1ceac08438070410189d3b4201729f84d62ef0115142cadea5180dc94c7c72437bfc47b57080c18ae33228b0c96e2ae4326854171bd3a0652b0ec6a6b3693d0cea2245845ae1a931ffee79556b0af857ecac8f805b9dfcb3feb7c2e92701a631960fb465ecaef34063ef528b9bc3d9ff8c7e934dd60b8be238cd9ffbf01377de780b2147504a381e208b3a730bafad85aabf1a"}'
#
# print(request_body)
#
# t = request_body.decode("utf-8")
# print(t)
# t = json.loads(t)
# print(t)
#
# print(bytes_to_json(request_body))

from backend.api.comm.json_loader import vue_interface_cfg

def is_subset(this, in_this):
    return this.issubset(in_this)

# print("-")
# print(is_subset(["a"], ["a", "b"]))
# print(is_subset([], ["a", "b"]))
# print(is_subset(["a", "b", "c"], ["a", "b"]))
# print(is_subset({"a"}, {"b"}))
def check_params(path, method, headers_got, body_got):
    p = {
            "logout": {
                "POST": {
                    "headers": {
                        "access_token": True,
                        "refresh_token": True
                    },
                    "body": {"latitude": True,
                             "longitude": True,
                             }
                }
            },

            "locations": {
                "POST": {
                    "headers": {
                        "access_token": True,
                        "refresh_token": True
                    },
                    "body": {"latitude": True,
                             "longitude": True,
                             }
                },

                "<str>": {
                    "GET": {
                        "headers": {
                            "access_token": True,
                            "refresh_token": True
                        },
                        "body": {"latitude": True,
                                 "longitude": True,
                                 }
                    },
                }
            },

    }

    path_as_list = [i for i in path.split("/") if i]

    not_found = False
    while path_as_list:

        current_path_segment = path_as_list.pop(0)
        re_found = False
        if current_path_segment not in p:
            for k, v in DEFAULT_CONVERTERS.items():
                if f"<{k}>" in p:
                    match = re.match(DEFAULT_CONVERTERS[k].regex,
                                     current_path_segment)
                    if match:
                        # fixme what if multiple paths contain same regex ie
                        #   a/<str>/b
                        #   a/<str>/c
                        re_found = True
                        p = p[f"<{k}>"]
                        break
            if not re_found:
                not_found = True
                break
        if not re_found:
            p = p[current_path_segment]

    if not_found:
        print(f"missing path {path}")
        return False

    if method not in p:
        print(f"missing {method=}")
        return False
    p = p[method]


    body_expected = {k for k,v in p["body"].items() if v}
    headers_expected = {k for k, v in p["headers"].items() if v}


    headers_test =   set(headers_got) <= set(headers_expected)

    body_test =  set(body_got) <= set(body_expected)

    if not headers_test:
        print(f"headers missing {headers_expected - headers_got}")

    if not body_test:
        print(f"body missing {body_expected - body_got}")

    print(f"returning {headers_test and body_test}")
    return headers_test and body_test

if __name__ == '__main__':

    print(check_params("logout", "POST",
                       {"access_token", "refresh_token"}, {"latitude", "longitude"}))
    print(True)
    print(80 * "-")
    print(check_params("logout", "GET",
                       {"access_token", "refresh_token"}, {"latitude", "longitude"}))
    print(False)
    print(80 * "-")
    print(check_params("logout", "POST",
                       {"r", "refresh_token"}, {"latitude", "longitude"}))
    print(False)
    print(80 * "-")
    print(check_params("logout", "POST",
                       {"access_token", "refresh_token"}, {"r", "longitude"}))
    print(False)
    print(80 * "-")
    print(check_params("locations/a", "GET",
                       {"access_token", "refresh_token"}, {"latitude", "longitude"}))
    print(True)
    print(80 * "-")

    print(check_params("/a", "GET",
                       {"access_token", "refresh_token"}, {"latitude", "longitude"}))
    print(False)
    print(80 * "-")
# print(check(["aggregator"], "/a/b/", "GET"))
# print(True)
# print(80 * "-")
# print(check(["aggregator"], "/a/", "GET"))
# print(False)
# print(80 * "-")
# print(check(["aggregator"], "/locations/a", "GET"))
# print(True)
# print(80 * "-")
# print(check(["aggregator"], "/m/locations/1", "GET"))
# print(True)
# print(80 * "-")
# print(check(["aggregator"], "/m/1/a", "GET"))
# print(False)
# print(80 * "-")