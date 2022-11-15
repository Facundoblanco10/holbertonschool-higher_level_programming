#!/usr/bin/python3
"""
   script that prints all City objects
   from the database hbtn_0e_14_usa:
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import Base, City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for row in cities:
        print("{}: ({}) {}".format(row.State.name,
                                   row.City.id,
                                   row.City.name))
