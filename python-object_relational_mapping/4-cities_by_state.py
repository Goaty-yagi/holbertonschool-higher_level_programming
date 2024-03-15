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
            query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id
            """
            cursor.execute(query)
            states = cursor.fetchall()
            for state in states:
                print(state)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
