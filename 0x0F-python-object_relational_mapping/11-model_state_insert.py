#!/usr/bin/python3
''' comment '''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    host = 'localhost'
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))
    session = sessionmaker(bind=engine)
    Session = session()

    insertState = State(name="Louisiana")
    Session.add(insertState)
    Session.commit()

    print("{}".format(insertState.id))

    Session.close()
