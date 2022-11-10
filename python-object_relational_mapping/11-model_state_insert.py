#!/usr/bin/python3
"""
    script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine, insert

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_obj = State(name='Louisiana', )
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
