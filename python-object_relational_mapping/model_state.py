#!/usr/bin/python3
"""
python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            '?host=localhost?port=3306'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)
Base.metadata.create_all(engine)
class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)

