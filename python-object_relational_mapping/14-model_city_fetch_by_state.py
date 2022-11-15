#!/usr/bin/python3
"""
   script that prints all City objects
   from the database hbtn_0e_14_usa:
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id):
        state_name = ''
        for state in session.query(State):
            if city.state_id == state.id:
                state_name = state.name
        print("{}: ({}) {}".format(state_name,
                                   city.id,
                                   city.name))
