import enum

from decouple import config

# class ROLES(enum.Enum):
#     AGGREGATOR = 'aggregator'
#     BUILDING_MANAGER = 'building_manager'
#     AGGREGATOR_AND_MANAGER = 'aggregator_and_building_manager'

#
# class ACTIONS(enum.Enum):
#     ADD = 'add'
#     GET_ALL = 'get all'
#     DELETE = 'delete'


MIDDLEWARE_NO_ACTION = config("CONFIG_DEFAULT_ACTION")
# MIDDLEWARE_ACTION_DENIED = False
INTERNAL_SERVER_ERROR_MESSAGE = "internal server error"

# prefix = "locations;"

#
# class LOCATION_ACTION(enum.Enum):
#     ADD_SINGLE = f'{prefix}create single'
#     DELETE_SINGLE = f"{prefix}delete single"
#     SELECT_BY_USERNAME = f"{prefix}select username"
#     SELECT_ALL = f"{prefix}select all"


# from backend.api.comm.json_loader import role_validation_cfg
# from collections import defaultdict


# def make_id_from_route_and_action(route, action):
#     # print(f"{route};{action}")
#     return route + ";" + action
#
#
# def get_actions_for_routes():
#     r_actions = defaultdict(set)
#     for role, route in role_validation_cfg["roles"].items():
#         for r, actions in route.items():
#             r_actions[r].update(
#                 {*[make_id_from_route_and_action(r, i) for i in list(actions)]})
#
#     return r_actions

# if __name__ == '__main__':
#     """"""
#     # with csv.reader()

# r_to_action = get_actions_for_routes()
# print(r_to_action)


# print(location_actions)
