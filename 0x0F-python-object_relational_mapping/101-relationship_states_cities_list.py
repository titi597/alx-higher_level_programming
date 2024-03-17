#!/usr/bin/python3
"""Script to list all State and City objects contained
in the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to get all State objects and their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Iterate over each State object
    for state in states:
        print("{}: {}".format(state.name, len(state.cities)))
        # Iterate over each City object associated with the State
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
