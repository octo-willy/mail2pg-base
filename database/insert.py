#database INSERT functions
import psycopg2
from psycopg2.extras import execute_values

INSERT_DATA = "INSERT INTO mytable (id,column1,column2) VALUES %s RETURNING id"

def add_data(conn,values):
    with conn,conn.cursor() as cursor:
        execute_values(cursor,INSERT_DATA,values)
        ids = [tup[0] for tup in cursor.fetchall()]
        return ids