#!/usr/bin/python3
''' lists all obj from db '''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                argv[2],
                                                                argv[3]))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
session.close()
