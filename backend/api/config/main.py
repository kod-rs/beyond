import enum


class ROLES(enum.Enum):
    AGGREGATOR = 'aggregator'
    BUILDING_MANAGER = 'building_manager'
    AGGREGATOR_AND_MANAGER = 'aggregator_and_building_manager'


class ACTIONS(enum.Enum):
    ADD = 'add'
    GET_ALL = 'get all'
    DELETE = 'delete'
