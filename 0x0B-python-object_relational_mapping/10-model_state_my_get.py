#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

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
    instanceCount = 0
    for instance in session.query(State).filter(State.name == sys.argv[4]):
        print(instance.id)
        instanceCount += 1
    if instanceCount == 0:
        print("Not found")
