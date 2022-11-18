#!/usr/bin/python3
"""
   script that creates the State “California” with the City “San Francisco”
   from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, MetaData

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)
    session.add(state)
    session.add(city)
    session.commit()
    session.close
