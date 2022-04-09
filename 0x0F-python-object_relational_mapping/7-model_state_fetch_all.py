#!/usr/bin/python3
''' lists all obj from db '''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for instance in states:
        print("{}: {}".format(instance.id, instance.name))
