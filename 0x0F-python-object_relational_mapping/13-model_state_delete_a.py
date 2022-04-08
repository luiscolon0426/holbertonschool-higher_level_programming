#!/usr/bin/python3
''' Script that deletes all state obj with a name with the
letter a from the database '''

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
    rows = session.query(State).from_statement(text(
        "SELECT * "
        "FROM states "
        "WHERE name REGEXP '^.*a.*' "
    )).all()
    for state in rows:
        session.delete(state)
    session.commit()
    session.close()
