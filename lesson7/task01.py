# Написать контекстный менеджер для работы с MySQL DB.

from lesson7 import test_config as config
import mysql.connector as mysql


class DBConnector:

    def __init__(self, connection_name):
        print("__init__")
        self._connection_name = connection_name
        self._connection = None
        self._cursor = None

    def __enter__(self):
        print("__enter__")
        try:
            self._connection = mysql.connect(**config.test_db)
        except mysql.Error as e:
            print('connection error', e)
        return self._connection

    def __exit__(self, *args):
        print("__exit__")
        self._connection.close()

    def __del__(self):
        print("__del__")


with DBConnector('test_db') as db:
    print("__main__")

    cursor = db.cursor()

    query = "SELECT version()"

    cursor.execute(query)

    for (version) in cursor:
        print(version)

    cursor.close()
