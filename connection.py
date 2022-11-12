from msilib.schema import Error
import sqlite3

def create_connection(DB_Manchester2022):
    conn = None
    try:
        conn = sqlite3.connect(DB_Manchester2022)
    except Error as e:
        print(e)

    return conn