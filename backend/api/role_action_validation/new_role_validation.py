import re

from django.urls.converters import DEFAULT_CONVERTERS
from backend.api.comm.json_loader import role_validation_cfg

def t(role, path, method):
    # print(role, path, method)
    config = role_validation_cfg

    # config = {
    #     "aggregator": {
    #         "logout": {
    #             "POST": True
    #         },
    #
    #         "locations": {
    #             "POST": True,
    #
    #             "<str>": {
    #                 "GET": True,
    #             }
    #         },
    #         "csrf": {
    #             "POST": True
    #         },
    #         "portfolio": {
    #             "GET": True,
    #             "POST": True
    #         },
    #         "login": {
    #             "POST": True
    #         },
    #
    #     }
    # }
    if role not in config:
        return False

    p = config[role]

    path_as_list = [i for i in path.split("/") if i]

    not_found = False
    while path_as_list:
        # print()
        # print(f"{path_as_list=}")
        # print(f"{p=}")

        current_path_segment = path_as_list.pop(0)
        # print(current_path_segment)
        re_found = False
        if current_path_segment not in p:
            for k, v in DEFAULT_CONVERTERS.items():
                if f"<{k}>" in p:
                    # print(f"test for {k}")
                    match = re.match(DEFAULT_CONVERTERS[k].regex,
                                     current_path_segment)
                    if match:
                        # fixme what if multiple paths contain same regex ie
                        #   a/<str>/b
                        #   a/<str>/c
                        re_found = True
                        p = p[f"<{k}>"]
                        break
                    # print(f"{match=}")
            if not re_found:
                not_found = True
                break
        if not re_found:
            p = p[current_path_segment]

    if not not_found:
        if method in p:
            # print("found method")
            return p[method]

    return False


def check(role, path, method):
    return any(t(i, path, method) for i in role)


def main():
    print(check(["aggregator"], "/locations", "GET"))
    print(True)
    print(80 * "-")
    print(check(["aggregator"], "/locations", "r"))
    print(False)
    print(80 * "-")
    print(check(["aggregator"], "/a/b/", "GET"))
    print(True)
    print(80 * "-")
    print(check(["aggregator"], "/a/", "GET"))
    print(False)
    print(80 * "-")
    print(check(["aggregator"], "/locations/a", "GET"))
    print(True)
    print(80 * "-")
    print(check(["aggregator"], "/m/locations/1", "GET"))
    print(True)
    print(80 * "-")
    print(check(["aggregator"], "/m/1/a", "GET"))
    print(False)
    print(80 * "-")


if __name__ == '__main__':
    main()
