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
            query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id
            """
            cursor.execute(query, (state,))
            states = cursor.fetchall()
            for index, state in enumerate(states):
                print(state[0], end=", " if index != len(states) - 1 else "\n")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <username> <password> <database> <state>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    list_cities(username, password, database, state)
