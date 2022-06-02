import pathlib
import sqlite3


class SQLiteCursor:

    def __init__(self, db_path=pathlib.Path().resolve() / "db"):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def create_tables():
    with SQLiteCursor() as cur:
        cur.execute("PRAGMA foreign_keys = ON")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Device (
                device_id int NOT NULL PRIMARY KEY,
                data_id INT NOT NULL,
                type TEXT NOT NULL,
                consumption REAL NOT NULL,
                FOREIGN KEY (data_id) REFERENCES Data(data_id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Location (
                location_id int NOT NULL PRIMARY KEY,
                latitude REAL NOT NULL, 
                longitude REAL NOT NULL, 
                section TEXT NOT NULL, 
                type TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS User (
                user_id int NOT NULL PRIMARY KEY,
                role TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Data (
                data_id int NOT NULL PRIMARY KEY,
                location_id int NOT NULL, 
                manager_id int NOT NULL,
                aggregator_id int NOT NULL ,
                timestamp TEXT NOT NULL, 
                value REAL NOT NULL, 
                predicted int NOT NULL,
                FOREIGN KEY(location_id) REFERENCES Location(location_id),
                FOREIGN KEY(manager_id) REFERENCES User(user_id),
                FOREIGN KEY(aggregator_id) REFERENCES User(user_id)
            )
        """)


def print_info():
    with SQLiteCursor() as cur:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        [print(i["name"]) for i in cur.fetchall()]
        print()

        cur.execute("PRAGMA table_info(Device)")
        [print(
            f'{i["cid"]:10}, '
            f'{i["name"]:20}, {i["type"]:10}, {i["notnull"]:10}, '
            f'{i["dflt_value"]}, {i["pk"]:10}')
         for i in cur.fetchall()]
        print()

        cur.execute("PRAGMA foreign_key_list(Device)")
        [print(i["id"], i["seq"], i["table"], i["from"], i["to"],
               i["on_update"], i["on_delete"], i["match"]) for i in
         cur.fetchall()]


def main():
    create_tables()

    print_info()


if __name__ == '__main__':
    main()
