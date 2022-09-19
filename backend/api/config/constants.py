import enum

from decouple import config

# class ROLES(enum.Enum):
#     AGGREGATOR = 'aggregator'
#     BUILDING_MANAGER = 'building_manager'
#     AGGREGATOR_AND_MANAGER = 'aggregator_and_building_manager'

MIDDLEWARE_NO_ACTION = config("CONFIG_DEFAULT_ACTION")
INTERNAL_SERVER_ERROR_MESSAGE = "internal server error"
