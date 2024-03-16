#!/usr/bin/python3
"""Create State California row with City San Francisco
"""
import sys

from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)
        session.add(new_state, new_city)
        session.commit()
