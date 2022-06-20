import json
import random
import string

import psycopg2
import requests
from decouple import config


class PostgresCursor:

    def __init__(self, config):
        self.conn = psycopg2.connect(**config)

    def __enter__(self):
        # self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, _type, value, traceback):
        self.conn.commit()
        self.conn.close()


def seed_users(config, users):
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
                    str(random.randint(1, 2)),
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
    seed_users(db_config, users)


if __name__ == '__main__':
    main()
