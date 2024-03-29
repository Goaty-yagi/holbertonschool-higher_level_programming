#!/usr/bin/python3
"""Print first row in the state table
"""
import sys

from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine

from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = session.query(State).order_by(State.id).all()
        for state in query:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print("    ", end='')
                print(f"{city.id}: {city.name}")
