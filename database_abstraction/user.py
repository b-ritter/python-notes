from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from address import Address
from base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    addresses = relationship("Address", order_by=Address.id, back_populates="user")
    
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password
        )
