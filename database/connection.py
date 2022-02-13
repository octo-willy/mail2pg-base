#database connection 
from multiprocessing import context
import os
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

#initialize a simple connection pool 
pool = SimpleConnectionPool(minconn=1,maxconn=5,
                            user=os.environ.get("USER"),
                            password = os.environ.get("PASSWORD"),
                            host = os.environ.get("HOSTNAME"),
                            port = os.environ.get("PORTNUMBER"),
                            database = os.environ.get("DATABASENAME"))

#connection handler
@contextmanager
def get_conn():
    try:
        connection = pool.getconn()
        yield connection
    except (Exception, psycopg2.Error) as e:
        print(f"Error while transaction: {e}")
    finally:
        pool.putconn(connection)