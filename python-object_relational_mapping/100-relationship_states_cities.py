#!/usr/bin/python3

"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pwd, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()

    session.close()
