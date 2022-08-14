import json
import pathlib

from backend.api.middleware.comm import middleware_check_params


def join_with_curr_path(p):
    curr_path = pathlib.Path(__file__).parent.resolve()
    return curr_path / p


def _get_config(config_name, curr_dir=True):
    if curr_dir:
        with open(join_with_curr_path(config_name)) as f:
            return json.loads(f.read())
    else:
        with open(config_name) as f:
            return json.loads(f.read())


vue_interface_path = pathlib.Path(__file__).parent.parent.parent.parent / "public" / "api_scheme" / "params.json"

role_validation_cfg = _get_config("role_validation.json")
vue_interface_cfg = _get_config(vue_interface_path, curr_dir=False)

for route, actions in vue_interface_cfg.items():
    for a, k in actions.items():
        actions[a] = list(k)
# print(vue_interface_cfg)


def main():
    """"""
    print(80 * "-")
    # i = _get_config(vue_interface_path, curr_dir=False)
    # print(i)
    # for route,w

    for r_k, r_v in {"csrf":True, "falseRoute":False}.items():

        t = middleware_check_params(vue_interface_cfg, r_k, "synchronizer", ["access_token", "refresh_token", "action"])
        print(t)


    t = middleware_check_params(vue_interface_cfg, "csrf", "synchronizer", ["access_token", "refresh_token", "action"])
    if not t:
        raise Exception()
    t = middleware_check_params(vue_interface_cfg, "csrf", "synchronizer", ["d", "access_token", "refresh_token", "action"])
    if not t:
        raise Exception()

    t = middleware_check_params(vue_interface_cfg, "x", "synchronizer", ["access_token", "refresh_token", "action"])
    if t:
        raise Exception()

    t = middleware_check_params(vue_interface_cfg, "csrf", "x", ["access_token", "refresh_token", "action"])
    if t:
        raise Exception()

    t = middleware_check_params(vue_interface_cfg, "csrf", "synchronizer", ["x"])
    if  t:
        raise Exception()

    t = middleware_check_params(vue_interface_cfg, "csrf", "synchronizer", ["f", "refresh_token", "action"])
    if t:
        raise Exception

    print("all ok")



if __name__ == '__main__':
    main()
