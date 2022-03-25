from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# Engine is the core interface to the database
engine = create_engine('mysql://geneva:Geneva2022!@localhost/dbdemo', echo=True)

# Create a databsae session, bind to the engine and prepare to use
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Base class for declaring tables
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    username = Column(String(50), unique=True)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', username='%s')>" % (self.name, self.fullname, self.username)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    type = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates = "addresses")

    
    def __repr__(self):
        return "<Addresses(address='%s', type='%s', user_id='%s')>" % (self.address, self.type, self.user_id)


User.addresses = relationship("Address", order_by = Address.id, back_populates = "user")