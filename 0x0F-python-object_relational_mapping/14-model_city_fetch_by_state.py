#!/usr/bin/python3
""" SQLAlchemy """

from sqlalchemy import create_engine
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(City, State).join(State).order_by(City.id).all()
    for i in q:
        print("{}: ({}) {}".format(i[1].name, i[0].id, i[0].name))
    session.close()
