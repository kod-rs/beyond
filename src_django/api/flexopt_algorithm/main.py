import sys
import pandas as pd
import numpy as np
import calendar
from typing import List, Union, NamedTuple
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from kneed import KneeLocator

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


def algorithm():
    df = pd.read_csv('active im en.csv')
    df = df.drop(['Unnamed: 0'], axis=1).reset_index(drop=True)

    ids = ('ZIV0034902130', 'ZIV0034902131', 'ZIV0034704030', 'ZIV0034703915',
           'ZIV0034704013',
           'ZIV0034703953', 'ZIV0034703954')
    length = len(ids)

    buildings = [df[_id].values for _id in ids]

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


if __name__ == '__main__':
    sys.exit(algorithm())
