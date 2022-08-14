from decouple import config
# from backend.api.role_action_validation.comm import deserialize_action_composite
# from backend.api.role_action_validation.role_validator import deserialize_action_composite
from backend.api.startup import startup_configuration
from backend.api.comm.json_loader import vue_interface_cfg

class DebuggableMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        self.debug = config("DEBUG") != "0"

    def log(self, payload):
        if self.debug:
            print(payload)


def middleware_check_params(action_composite, given):
    """check if all parameters are present that are required for this request"""

    route, action = startup_configuration\
        .get_scheme_validator()\
        .deserialize(action_composite)

    if route not in vue_interface_cfg:
        # print(f"no route {route}")
        return False

    r = vue_interface_cfg[route]

    if action not in r:
        # print(f"no action {action}")
        return False

    r = r[action]
    # print(f"expecting {r}")
    return all([given.__contains__(i) for i in r])
