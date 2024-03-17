#!/usr/bin/python3
"""Print first row in the state table
"""
import sys

from sqlalchemy.orm import sessionmaker, joinedload
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
    Session = sessionmaker(bind=engine)
    with Session() as session:
        query = session.query(City).order_by(City.id).all()
        for city in query:
            print(f"{city.id}: {city.name} -> {city.state.name}")
