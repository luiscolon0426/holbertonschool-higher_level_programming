#!/usr/bin/python3
''' comment '''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
session = Session()
new_state = State(name='Louisiana')
session.add(new_state)
state = session.query(State).filter_by(name='Louisiana').first()
print(str(state.id))
session.commit()
session.close()
