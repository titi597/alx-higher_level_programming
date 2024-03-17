#!/usr/bin/python3
"""Script to create the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa"""

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

    # Create a new State object
    california = State(name="California")

    # Create a new City object
    san_francisco = City(name="San Francisco")

    # Add the City to the State
    california.cities.append(san_francisco)

    # Add the State and City to the session
    session.add(california)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()
