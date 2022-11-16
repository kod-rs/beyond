import calendar
import datetime
import typing
from operator import itemgetter
from typing import List, Union, NamedTuple

import numpy
import numpy as np
import pandas as pd
from kneed import KneeLocator
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

MIN_VALUE = 500
MAX_VALUE = 2500
NUMBER_OF_SAMPLES = 8760
TIME_RESOLUTION = 3600  # [s], 1/sample_rate
N_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTHS = tuple(calendar.month_name[1:])
MAX_H_IN_DAY = 24
H_IN_DAY = list(range(MAX_H_IN_DAY))

point_coordinates = List[Union[int, float]]


class BuildingEnergy(NamedTuple):
    building_id: str
    energy_info: typing.List['EnergyInfo']


class EnergyInfo(NamedTuple):
    timestamp: datetime.datetime
    value: float


class TimeInterval(NamedTuple):
    from_t: datetime.datetime
    to_t: datetime.datetime


class CurrentBuildingInfo(NamedTuple):
    building_id: str
    time_interval: TimeInterval
    flex: float


def is_outlier(label: int) -> bool:
    """
    Function that checks if the point in an outlier.
    Args:
        label: -1 if outlier, else positive integer

    Returns:
        True if point is an outlier, else False
    """
    return label == -1


def is_first_cluster(label: int) -> bool:
    """
    Function that checks if the point is in the first cluster.
    Args:
         label: 0 if in first cluster, else non-zero integer

    Returns:
        True if in first cluster, else False
    """
    return label == 0


def is_in_range(value: Union[int, float]) -> bool:
    """
    Function that checks if the point is in given range.
    Args:
        value: y coordinate

    Returns:
        True if in range, else False
    """
    return MIN_VALUE <= value < MAX_VALUE


def selected_points(list_of_all_points: point_coordinates,
                    labels: np.ndarray) -> List[point_coordinates]:
    """
       Only considering if there is more than one cluster.
    Args:
        list_of_all_points: Points to be considered
        labels: Array that connects each point with its cluster

    Returns: list of points to consider for flexibility
    """
    if max(labels) <= 0:
        return []

    filtered = []
    for hour, value, label in zip(list_of_all_points[:, 1],
                                  list_of_all_points[:, 0],
                                  labels):
        if (not is_outlier(label)
                and not is_first_cluster(label)
                and is_in_range(value)):
            filtered.append([hour, value])
    return filtered


def finding_elbow_of_the_graph(point_list: np.array) -> float:
    """
    Function that calculates the distances of every point to their nearest
    neighbor, sorts them and finds the "elbow".
    Args:
        point_list: List of (y,x) tuples

    Returns:
        y elbow value
    """
    neighbors = NearestNeighbors(n_neighbors=8)
    nearest_neighbors = neighbors.fit(point_list)
    distances, indices = nearest_neighbors.kneighbors(point_list)
    distances: np.ndarray = np.sort(distances, axis=0)
    distances: np.ndarray = distances[:, 1]
    knee = KneeLocator(range(len(distances)), distances, curve='convex',
                       direction='increasing')
    return knee.knee_y


def difference_calculation(points: numpy.ndarray) -> List[tuple]:
    """
    Function that calculates min, mid and max baseline with which the input
    data can be described.
    Then it calculates the difference between mid and max.
    Args:
        points: points to be considered

    Returns:
        List of tuples; where each tuple contains x (represents
        hour in a day) and difference between max and mid baseline
    """
    last_hour = 23
    min_base = []
    max_base = []

    a = points.tolist()
    b = sorted(a, key=itemgetter(0, 1))

    alert = 0
    current_hour = 0
    for x, y in enumerate(b):
        if alert == 0:
            min_base.append(y)
            alert = 1
            current_hour = y[0]
        elif y[0] == current_hour:
            continue
        elif y[0] != current_hour:
            max_base.append(b[x - 1])
            min_base.append(y)
            current_hour = y[0]
    max_base.append(y)

    if min_base[-1][0] != last_hour:
        min_base.insert(last_hour, [last_hour, min_base[-1][1]])
        max_base.insert(last_hour, [last_hour, min_base[-1][1] + (
                max_base[-1][1] - min_base[-1][1]) / 2])

    if min_base[0][0] != 0:
        min_base.insert(0, [0, min_base[-1][1]])
        max_base.insert(0, [0, min_base[-1][1] + (
                max_base[-1][1] - min_base[-1][1]) / 2])

    for sat in range(MAX_H_IN_DAY):
        if min_base[sat][0] != sat:
            min_base.insert(sat, [sat, np.nan])
            max_base.insert(sat, [sat, np.nan])
    min_base = np.array(min_base)
    max_base = np.array(max_base)

    temp_min: list = pd.Series(min_base[:, 1]).interpolate(method="linear",
                                                           order=1).tolist()
    temp_max: list = pd.Series(max_base[:, 1]).interpolate(method="linear",
                                                           order=1).tolist()
    min_base = np.array(min_base)
    min_base[:, 1] = temp_min
    max_base = np.array(max_base)
    max_base[:, 1] = temp_max

    diff = []

    for x, val1, val2 in zip(min_base[:, 0], min_base[:, 1], max_base[:, 1]):
        diff.append((x, (val2 - val1) / 2))

    return diff


def get_points(building_ids: tuple, buildings: list, interval: TimeInterval
               ) -> List[List[point_coordinates]]:
    """

    Args:
        building_ids: tuple of strings
        buildings: timeseries values keyed by building id
        interval: time period

    Returns:
        List of (x, y) points to be considered in further calculations
    """
    month_index = interval.from_t.month - 1
    month_days = N_DAYS[month_index]
    points = []
    hour_accumulator = sum(N_DAYS[:month_index]) * 24
    for building_id in range(len(building_ids)):
        month_hours: list = month_days * H_IN_DAY

        inverted_point_list = np.array(
            [buildings[building_id][hour_accumulator: hour_accumulator
                                                      + month_days
                                                      * MAX_H_IN_DAY],
             month_hours]).transpose()

        elbow = finding_elbow_of_the_graph(inverted_point_list)
        eps, min_samples = [elbow, 8] if elbow <= 20 else [20, 16]
        dbscan = DBSCAN(eps=eps,
                        min_samples=min_samples).fit(inverted_point_list)

        labels: np.ndarray = dbscan.labels_

        points.append(selected_points(inverted_point_list, labels))
    return points


def get_max_diff(building_ids: tuple, points: List[List[point_coordinates]]
                 ) -> List[Union[str, List[tuple]]]:
    """
    Calculate the maximum difference between the middle baseline and the
        extremity baseline for all buildings.
    Args:
        building_ids: building ids
        points: list of (x, y), where x = current hour, y = consumption

    Returns:
        List of lists; where first element is building_id and second is list of
        tuples; where first element is hour in a day and second is differences
        between the middle baseline and the extremity baseline at that hour

    """
    max_diff = []
    no_flex = [[i, 0] for i in range(MAX_H_IN_DAY)]
    for index, building_id in enumerate(building_ids):
        points_by_building = points[index]
        if len(points_by_building) > 40:
            points_by_building = np.array(points_by_building)
            diff = difference_calculation(points_by_building)
            max_diff.append([building_id, diff])
        else:
            max_diff.append([building_id, no_flex])
    return max_diff


def add_sort(diffs: np.ndarray, interval: TimeInterval
             ) -> List[List[Union[int, float]]]:
    """
    Function adds the diffs, takes 20% and sorts the results
    descendingly according to the flexibility.
    Args:
        diffs:  Differences
        interval: Time period

    Returns: Sorted flexibility

    """
    ret = []
    for building in range(len(diffs)):
        from_h = interval.from_t.hour
        to_h = interval.to_t.hour
        if sum(np.array(diffs[building][1][from_h: to_h])[:, 1]) > 0:
            res = np.array(diffs[building][1][from_h:to_h])
            res = round(sum(res[:, 1]) * 0.2, 2)
            ret.append([building, res])

    return sorted(ret, key=itemgetter(1), reverse=True)


def confidence(flex_list: List[List[Union[int, float]]],
               flex_amount: float) -> List[tuple]:
    """
    Function that calculates confidence for a building.
    Args:
        flex_list: List of possible flexibilities
        flex_amount: Needed amount of flexibility

    Returns:
        Tuple containing building number and corresponding confidence factor
    """

    return [(f[0], round(f[1] / flex_amount, 2)) for f in flex_list]


def apply_flexibility(diffs: List[Union[str, List[tuple]]],
                      interval: TimeInterval, flex: float
                      ) -> List[CurrentBuildingInfo]:
    """
    Calculate flexibility per time and per building.
    Args:
        diffs: List of N lists, where 'N' is the number of buildings. Every
        list contains two elements, where the first is building_id (str) and
         the second is list of tuples (hour, diff).
        interval: Interval when the flexibility is needed
        flex: Amount of flexibility needed

    Returns:
        How much flexibility can a building give and when

    """

    order = add_sort(np.array(diffs, dtype=object), interval)
    ret = []

    from_h = interval.from_t.hour
    to_h = interval.to_t.hour

    for building in range(len(order)):
        flex_amount = 0

        if flex > 0:
            if order[building][1] >= flex:
                start = -1
                for hour in range(from_h, to_h):
                    if (diffs[order[building][0]][1][hour][1] > 0
                            and start == -1):
                        start = hour
                    if flex <= diffs[order[building][0]][1][hour][1]:
                        flex_amount += flex
                        end = hour + 1
                        break
                    else:
                        flex_amount += diffs[order[building][0]][1][hour][1]
                        flex -= diffs[order[building][0]][1][hour][1]

                start = interval.from_t.replace(hour=start)
                end = interval.to_t.replace(hour=end)
                ret.append(CurrentBuildingInfo(
                    building_id=diffs[order[building][0]][0],
                    time_interval=TimeInterval(start, end),
                    flex=round(flex_amount, 2)))
                break
            else:
                flex -= order[building][1]
                for hour in range(from_h, to_h):
                    if diffs[order[building][0]][1][hour][1] > 0:
                        start = hour
                        break
                for hour in reversed(range(from_h, to_h)):
                    if diffs[order[building][0]][1][hour][1] > 0:
                        end = hour + 1
                        break
                start = interval.from_t.replace(hour=start)
                end = interval.to_t.replace(hour=end)
                ret.append(CurrentBuildingInfo(
                    building_id=diffs[order[building][0]][0],
                    time_interval=TimeInterval(start, end),
                    flex=round(order[building][1], 2)))
        else:
            break

    return ret


def algorithm(building_energy_list: typing.List[BuildingEnergy],
              interval: TimeInterval,
              flex_amount: int) -> typing.Tuple[float,
                                                List[CurrentBuildingInfo]]:
    """
    Flexibility optimization algorithm.
    Get the available flexibility for the requested interval.
    Args:
        building_energy_list: building id paired with its timeseries data
        interval: requested interval
        flex_amount: requested flexibility amount
    Returns:
        Total flexibility and flexibility per building for the interval

    """
    building_ids = tuple(b.building_id for b in building_energy_list)
    buildings = [[b_list.value for b_list in b.energy_info]
                 for b in building_energy_list]

    points = get_points(building_ids, buildings, interval)

    max_diff = get_max_diff(building_ids, points)

    building_info_list = apply_flexibility(max_diff, interval, flex_amount)

    total_flex = sum([building.flex for building in building_info_list])

    return total_flex, building_info_list
