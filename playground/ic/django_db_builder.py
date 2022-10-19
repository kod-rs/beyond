import sys
import csv
import sqlite3
import sys
from pathlib import Path

import requests


def main():
    with open('active im en.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file))
    building_ids = [building_id for building_id in csv_reader[0][2:]]
    csv_reader = csv_reader[1:]
    for row_no, row in enumerate(csv_reader):
        timestamp = row[1]
        buildings_data = row[2:]
        for column_no, building_data in enumerate(buildings_data):
            values = (building_data, timestamp, building_ids[column_no])

            response = requests.post()



if __name__ == '__main__':
    sys.exit(main())
