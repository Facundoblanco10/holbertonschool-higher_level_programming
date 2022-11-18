#!/usr/bin/python3
"""
python file that contains the class definition of a
City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """state class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
