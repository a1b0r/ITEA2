import config
import mysql.connector


def get_version():
    con = mysql.connector.connect(**config.config)

    cursor = con.cursor()

    query = "SELECT version()"

    cursor.execute(query, )

    for (version) in cursor:
        print(version)
    cursor.close()
    con.close()


get_version()
