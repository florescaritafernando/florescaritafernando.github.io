import sqlite3

try:
    conn = sqlite3.connect("database/db_manchester.db")
    cursor=conn.cursor()
    cursor.execute("select * from tb_diseno_color")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)

