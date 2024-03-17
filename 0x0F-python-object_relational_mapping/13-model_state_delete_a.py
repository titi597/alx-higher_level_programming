#!/usr/bin/python3
"""Script to delete State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects with a name containing the letter 'a'
    states_to_delete = session.query(State)\
                              .filter(State.name.like('%a%'))\
                              .all()

    # Delete each State object in the query result
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to the database
    session.commit()

    # Close the session
    session.close()
