#!/usr/bin/python3
"""
   script that deletes all State objects with a name
   containing the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    for state in session.query(State).order_by(State.id):
        if state.name.find('a') == -1:
            session.delete(state)
            session.commit()
