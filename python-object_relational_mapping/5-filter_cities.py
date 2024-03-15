#!/usr/bin/python3
'''
This script is to connect DB from python.
'''
import sys

import MySQLdb


def list_cities(
    username: str,
    password: str,
    database: str,
    state: str
) -> None:
    """
    This function prints all states where in the DB received as args.
    """
    with MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    ) as connection:

        with connection.cursor() as cursor:
            query = "SELECT cities.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;"
            cursor.execute(query, (state,))
            cities = cursor.fetchall()
            print(", ".join([city[0] for city in cities]))


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state = sys.argv[4]

        list_cities(username, password, database, state)
