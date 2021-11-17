#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy.orm import session, sessionmaker
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.id == "2"):
        instance.name = "New Mexico"
    session.commit()
