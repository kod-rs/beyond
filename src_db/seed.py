import json
import random
import string
import time

import psycopg2
import requests
from decouple import config

import datetime


class PostgresCursor:

    def __init__(self, config):
        self.conn = psycopg2.connect(**config)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, _type, value, traceback):
        self.conn.commit()
        self.conn.close()


def seed_api_user(config, users):
    with PostgresCursor(config) as cur:
        letters = string.ascii_lowercase

        for i, p in enumerate(users):
            cur.execute(
                """
                insert into api_user (username, password, role_id)
                values (%s, %s, %s)
                """,
                (
                    f'{p.first_name}_{p.last_name}',
                    ''.join(random.choice(letters) for _ in range(10)),
                    random.randint(1, 3),
                )
            )


def seed_auth_user(config, users):
    with PostgresCursor(config) as cur:
        letters = string.ascii_lowercase

        for i, p in enumerate(users):
            cur.execute(
                """
                insert into auth_user (
                username, password, is_superuser, first_name,
                last_name,
                email,
                is_staff,
                is_active,
                date_joined
                
                )
                values (%s,%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    f'{p.first_name}_{p.last_name}',
                    ''.join(random.choice(letters) for _ in range(10)),
                    False,
                    p.first_name,
                    p.last_name,
                    f'{p.first_name}_{p.last_name}@tmp.com',
                    False,
                    True,
                    datetime.datetime.now()

                    # random.randint(1, 3),
                )
            )

class User:

    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar


def load_users():
    r = []

    for page in [1, 2]:
        url = f"https://reqres.in/api/users?page={page}"

        headers = {'Content-type': 'application/json'}
        res = requests.get(url, headers=headers)
        parsed_res = json.loads(res.text)

        r += [User(**p) for p in parsed_res["data"]]

    return r


def main():
    db_config = {
        "database": config("DB_NAME"),
        "user": config("DB_USER"),
        "password": config("DB_PASSWORD"),
        "host": config("DB_HOST"),
        "port": config("DB_PORT")
    }

    users = load_users()
    # seed_api_user(db_config, users)
    seed_auth_user(db_config, users)


if __name__ == '__main__':
    main()
