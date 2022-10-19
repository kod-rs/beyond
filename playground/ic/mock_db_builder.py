import csv
import sqlite3
import sys
from pathlib import Path


def main():
    db_path = Path(__file__).resolve().parents[2] / 'db.sqlite3'
    conn = create_connection(db_path)
    cur = conn.cursor()
    sql = ''' INSERT INTO data(value, timestamp,locationID) 
            VALUES(?,?,?)'''
    create_locations_table(cur)
    conn.commit()
    create_data_table(cur)

    with open('active im en.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file))

    building_ids = [building_id for building_id in csv_reader[0][2:]]
    create_mock_buildings(cur, building_ids)
    csv_reader = csv_reader[1:]
    for row_no, row in enumerate(csv_reader):
        timestamp = row[1]
        buildings_data = row[2:]
        for column_no, building_data in enumerate(buildings_data):
            values = (building_data, timestamp, building_ids[column_no])
            cur.execute(sql, values)
    conn.commit()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(
            db_file,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_locations_table(cur: sqlite3.Cursor):
    sql_delete = 'DROP TABLE IF EXISTS data'
    sql_create_data_table = """
    CREATE TABLE IF NOT EXISTS locations (
        locationID TEXT PRIMARY KEY,
        longitude REAL NOT NULL,
        latitude REAL NOT NULL);"""
    try:
        cur.execute(sql_delete)
        cur.execute(sql_create_data_table)
    except sqlite3.Error as e:
        print(e)


def create_data_table(cur: sqlite3.Cursor):
    sql_create_data_table = """
    CREATE TABLE data (
        dataID INTEGER PRIMARY KEY,
        value REAL NOT NULL,
        timestamp TIMESTAMP NULL,
        locationID REFERENCES locations(locationID));"""
    try:
        cur.execute(sql_create_data_table)
    except sqlite3.Error as e:
        print(e)


def create_mock_buildings(cur, building_ids):
    sql = '''INSERT OR IGNORE INTO locations(locationID, 
                                    longitude,
                                    latitude) 
                VALUES(?,?,?)'''
    values = [(b_id, index + 0.3, index + 0.5)
              for index, b_id in enumerate(building_ids)]
    for value in values:
        try:
            cur.execute(sql, value)
        except sqlite3.Error as e:
            print(e)


if __name__ == '__main__':
    sys.exit(main())
