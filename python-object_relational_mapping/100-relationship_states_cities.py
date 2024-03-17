#!/usr/bin/python3
"""Create State California row with City San Francisco
"""
import sys

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from relationship_state import Base, State, City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        new_city = City(name="San Francisco")
        new_state = State(name="California", cities=[new_city])

        session.add(new_state)
        session.add(new_city)
        session.commit()
