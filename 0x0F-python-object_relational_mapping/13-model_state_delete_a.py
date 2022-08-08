#!/usr/bin/python3
""" SQLAlchemy """


from sqlalchemy import create_engine, Column
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    deletea = session.query(State).filter(State.name.like('%a%'))
    for i in deletea:
        session.delete(i)
    session.commit()
    session.close()
