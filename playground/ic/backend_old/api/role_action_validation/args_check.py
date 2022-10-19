import re
from django.urls.converters import DEFAULT_CONVERTERS
from playground.ic.backend_old.api.comm.json_loader import vue_interface_cfg

def check_params(path, method, headers_got, body_got):
    print(path, method, headers_got, body_got)
    p  = vue_interface_cfg

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

    # todo maybe not safe, configurator skips this not on purpose ?
    if "body" not in p:
        body_expected = set()
    else:
        body_expected = {k for k,v in p["body"].items() if v}
    if "headers" not in p:
        headers_expected = set()
    else:
        headers_expected = {k for k, v in p["headers"].items() if v}

    headers_test =  set(headers_expected) <= set(headers_got)

    body_test = set(body_expected) <= set(body_got)

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