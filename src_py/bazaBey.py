import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute("CREATE TABLE Device ("
            "device_id int NOT NULL PRIMARY KEY,"
            "data_id INT NOT NULL,"
            "type TEXT NOT NULL, "
            "consumption REAL NOT NULL,"
            "FOREIGN KEY (data_id) REFERENCES Data(data_id))")

cur.execute("CREATE TABLE Location ("
            "location_id int NOT NULL PRIMARY KEY,"
            "latitude REAL NOT NULL, "
            "longitude REAL NOT NULL, "
            "section TEXT NOT NULL, "
            "type TEXT NOT NULL)")

cur.execute("CREATE TABLE User ("
            "user_id int NOT NULL PRIMARY KEY,"
            "role TEXT NOT NULL,"
            "password TEXT NOT NULL)")

cur.execute("CREATE TABLE Data ("
            "data_id int NOT NULL PRIMARY KEY,"
            "location_id int NOT NULL, "
            "manager_id int NOT NULL,"
            "aggregator_id int NOT NULL ,"
            "timestamp TEXT NOT NULL, "
            "value REAL NOT NULL, "
            "predicted int NOT NULL,"
            "FOREIGN KEY(location_id) REFERENCES Location(location_id),"
            "FOREIGN KEY(manager_id) REFERENCES User(user_id),"
            "FOREIGN KEY(aggregator_id) REFERENCES User(user_id))")

#cur.execute("PRAGMA foreign_key_list(Data)")
#print(cur.fetchall())

#list all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

cur.execute("PRAGMA table_info(Device)")
print(cur.fetchall())

cur.execute("PRAGMA foreign_key_list(Device)")
print(cur.fetchall())