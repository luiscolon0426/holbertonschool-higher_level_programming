#!/usr/bin/python3
''' Script that changes the name of a state '''

import MySQLdb
from sys import argv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).from_statement(text(
        "SELECT * "
        "FROM states "
        "WHERE id=2 "
    )).one()
    state.name = "New Mexico"
    session.commit()
    session.close()
