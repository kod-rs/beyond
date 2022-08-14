import enum


class ROLES(enum.Enum):
    AGGREGATOR = 'aggregator'
    BUILDING_MANAGER = 'building_manager'
    AGGREGATOR_AND_MANAGER = 'aggregator_and_building_manager'


class ACTIONS(enum.Enum):
    ADD = 'add'
    GET_ALL = 'get all'
    DELETE = 'delete'

class LOCATION_ACTION(enum.Enum):
    ADD_SINGLE = 'location add single'
    # ADD_MULTIPLE = "add multiple"
    # DELETE_SINGLE = "delete single"
    GET_BY_USERNAME = "location get username"
    GET_ALL = "location get all"

from backend.api.comm.json_loader import role_validation_cfg

MIDDLEWARE_NO_ACTION = role_validation_cfg["no action"]
MIDDLEWARE_ACTION_DENIED = False
INTERNAL_SERVER_ERROR_MESSAGE = "internal server error"