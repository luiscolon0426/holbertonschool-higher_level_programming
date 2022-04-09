#!/usr/bin/python3
'''
file similar to model_state.py named model_city.py that contains the class
definition of a City
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    '''
    Inherits from Base and links MySQL 'state'
    Instances:
        id: column of an auto-generated, unique integer
        name: column of a string with 128 characters max
        state_id: column of an integer can't be null and is a foreign key to
        states.id
    '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
