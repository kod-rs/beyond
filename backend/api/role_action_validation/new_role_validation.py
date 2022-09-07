import re

from django.urls.converters import DEFAULT_CONVERTERS

def try_pure(role, path, method, config):
    if role not in config:
        return False

    p = config[role]

    path_as_list = [i for i in path.split("/") if i]

    not_found = False
    while path_as_list:
        print()
        print(f"{path_as_list=}")
        print(f"{p=}")

        current_path_segment = path_as_list.pop(0)
        print(current_path_segment)
        if current_path_segment not in p:
            not_found = True
            break
        p = p[current_path_segment]

    if not not_found:
        if method in p:
            print("found method")
            return p[method]

    return False

def try_re(role, path, method, config):
    if role not in config:
        return False

    p = config[role]

    path_as_list = [i for i in path.split("/") if i]

    not_found = False
    while path_as_list:
        print()
        print(f"{path_as_list=}")
        print(f"{p=}")

        current_path_segment = path_as_list.pop(0)
        print(current_path_segment)
        re_found = False
        if current_path_segment not in p:
            for k,v in DEFAULT_CONVERTERS.items():
                if f"<{k}>" in p:
                    print(f"test for {k}")
                    match = re.match(DEFAULT_CONVERTERS[k].regex, current_path_segment)
                    if match:
                        # fixme what if multiple paths contain same regex ie
                        #   a/<str>/b
                        #   a/<str>/c
                        re_found = True
                        p = p[f"<{k}>"]
                        break
                    print(f"{match=}")
            if not re_found:
                not_found = True
                break
        if not re_found:
            p = p[current_path_segment]

    if not not_found:
        if method in p:
            print("found method")
            return p[method]

    return False


def t(role, path, method):
    print(role, path, method)

    config = {
        "aggregator": {
            "locations": {
                "GET": True,

            },
            "a": {
                "b": {
                    "GET": True
                }
            }
        },
    }

    config_re = {
        "aggregator": {
            "locations": {
                "<str>": {
                    "GET": True,

                }
            },
            "m": {
                "<str>": {
                    "<int>": {
                        "GET": True,

                    }

                }
            }
        }
    }

    r = try_pure(role, path, method, config)
    if r:
        return True
    print(40 * "=")
    r = try_re(role, path, method, config_re)
    if r:
        return True

    return False

    # current_path_segment = path.pop(0)
    # if current_path_segment not in p and not any(str(k).startswith("<") for k,_ in p.items()):
    #     return False
    #
    # p = p[current_path_segment]
    #
    # print(f"{p=}")
    # print(f"{path=}")
    #
    # # "int": IntConverter(),
    # # "path": PathConverter(),
    # # "slug": SlugConverter(),
    # # "str": StringConverter(),
    # # "uuid": UUIDConverter(),
    # match = re.match(DEFAULT_CONVERTERS["int"].regex, "28")
    # print(match)
    # # print(DEFAULT_CONVERTERS)
    #
    # return True




def check(role, path, method):
    return any(t(i, path, method) for i in role)


#
def main():
    # print("t")
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
    # print(check("role1", "action1"))
    # print(check("role1", "action2"))
    # print(check("role2", "action1"))
    # print(check("role2", "action2"))
    # print(check("role3", "action1"))
    # print(check("role3", "action2"))

if __name__ == '__main__':
    main()