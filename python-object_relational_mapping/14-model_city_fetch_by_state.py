#!/usr/bin/python3

"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pwd, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all())

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
