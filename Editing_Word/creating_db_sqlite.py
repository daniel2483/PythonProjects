import os
import sqlite3
from sqlite3 import Error

current_dir = os.getcwd()
print ("Current Directory: " + current_dir)

db_path = current_dir + "\db\pythonsqlite.db"
print ("Current DB Path: " + db_path)


def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(db_path)
