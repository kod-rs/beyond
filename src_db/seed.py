import pathlib
import random
import sqlite3
import json
import time

import requests

import psycopg2
from decouple import config


class SQLiteCursor:

    def __init__(self, db_path=pathlib.Path().resolve() / ".." / "db.sqlite3"):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, _type, value, traceback):
        self.conn.commit()
        self.conn.close()


class PostgresCursor:

    def __init__(self, config):
        self.conn = psycopg2.connect(**config)

    def __enter__(self):
        # self.conn = psycopg2.connect(**config)
        # self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, _type, value, traceback):
        self.conn.commit()
        self.conn.close()


def seed_users(users):

    with SQLiteCursor() as cur:
        for p in users:

            cur.execute(f"""insert into api_person (username, password) values
            (?, ?)
                        """, (p.first_name, str(random.randint(100, 200))))


class User:

    def __init__(self, id_, email, first_name, last_name, avatar):
        self.id = id_
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar


def load_users():
    url = "https://reqres.in/api/users?page=2"

    headers = {'Content-type': 'application/json'}
    res = requests.get(url, headers=headers)
    parsed_res = json.loads(res.text)

    return [User(**p) for p in parsed_res["data"]]


def main():
    users = load_users()
    seed_users(users)


if __name__ == '__main__':
    # main()

    # cur.execute("insert into api_user (id, username, password, role_id) values (%s, %s, %s, %s)", (1, "user 1", "pass 1", 1))

    db_config = {
        "database": config("DB_NAME"),
        "user": config("DB_USER"),
        "password": config("DB_PASSWORD"),
        "host": config("DB_HOST"),
        "port": config("DB_PORT")
    }


    with PostgresCursor(db_config) as cur:
        cur.execute("select * from api_user")
        rows = cur.fetchall()
        print(rows)
