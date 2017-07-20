""" Just the SQL Alchemy ORM tutorial """

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from user import User
from address import Address
from base import Base

engine = create_engine('sqlite:///:memory:', echo=True)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first()
    print(our_user.addresses)
    our_user.addresses = [Address(email_address="foo@bar.com")]
    print(our_user.addresses)
    print(our_user.addresses[0])
    print(our_user.addresses[0].user)