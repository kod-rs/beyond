import pathlib
import random
import sqlite3
import json
import time

import requests


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


def seed_person(persons):

    with SQLiteCursor() as cur:
        for p in persons:


            cur.execute(f"""insert into api_person (username, password) values
            (?, ?)
                        """, (p.first_name, str(random.randint(100, 200))))

class Person():

    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    def __repr__(self):
        return f"{self.id=} {self.email=} {self.first_name=} {self.last_name=} {self.avatar=}"

def load_person():
    url = "https://reqres.in/api/users?page=2"

    headers = {'Content-type': 'application/json'}
    res = requests.get(url, headers=headers)
    parsed_res = json.loads(res.text)

    r = []
    for p in parsed_res["data"]:
        r.append(Person(**p))

    return r

def main():
    persons = load_person()
    seed_person(persons)


if __name__ == '__main__':
    main()
