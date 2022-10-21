import calendar
import sys
from operator import itemgetter
from typing import List, Union

import numpy
import numpy as np
import pandas as pd
from kneed import KneeLocator
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

point_coordinates = List[Union[int, float]]

MIN_VALUE = 500
MAX_VALUE = 2500
NUMBER_OF_SAMPLES = 8760
TIME_RESOLUTION = 3600  # [s], 1/sample_rate
N_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTHS = tuple(calendar.month_name[1:])
MAX_H_IN_DAY = 24
H_IN_DAY = list(range(MAX_H_IN_DAY))


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


def selected_points(list_of_all_points: List[point_coordinates],
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


def baseline_calculation(points: numpy.ndarray) -> tuple:
    """
    Function that calculates min, mid and max baseline with which the input
    data can be described.
    It also calculates the difference between mid and max.
    Args:
        points: points to be considered

    Returns:
        A tuple containing (min, mid, max) and abs(mid - max).
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
    mid_base = []

    diff = []
    # TODO name this better
    for x, vr1, vr2 in zip(min_base[:, 0], min_base[:, 1], max_base[:, 1]):
        mid_base.append([x, (vr1 + vr2) / 2])
        diff.append([x, (vr2 - vr1) / 2])

    mid_base = np.array(mid_base)

    return min_base, max_base, mid_base, diff


def get_points(ids: tuple, buildings: list) -> dict:
    points = {month: [] for month in MONTHS}
    for building_id in range(len(ids)):
        hour_accumulator = 0

        for month_index, month_days in enumerate(N_DAYS):
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
            hour_accumulator += month_days * MAX_H_IN_DAY

            points[MONTHS[month_index]].append(
                selected_points(inverted_point_list, labels))
    return points


def get_max_diff(ids: tuple, points: dict) -> dict:
    max_diff = {month: [] for month in MONTHS}
    no_flex = [[i, 0] for i in range(MAX_H_IN_DAY)]
    for month_index in range(len(MONTHS)):
        for building_di in range(len(ids)):
            _points = points[MONTHS[month_index]][building_di]
            if len(_points) > 40:
                _points = np.array(_points)
                min_base, max_base, mid_base, diff = baseline_calculation(
                    _points)
                max_diff[MONTHS[month_index]].append(diff)
            else:
                max_diff[MONTHS[month_index]].append(no_flex)
    return max_diff


def algorithm():
    # TODO get this from somewhere else
    df = pd.read_csv('active im en.csv')
    df = df.drop(['Unnamed: 0'], axis=1).reset_index(drop=True)
    ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030', 'ZIV0034703915',
           'ZIV0034704013',
           'ZIV0034703953', 'ZIV0034703954')
    length = len(ids)
    buildings = [df[_id].values for _id in ids]
    points = get_points(ids, buildings)
    max_diff = get_max_diff(ids, points)

    breakpoint()
    pass


if __name__ == '__main__':
    sys.exit(algorithm())
