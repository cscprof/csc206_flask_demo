# import the framwework
from enum import unique
import os
import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
config = configparser.ConfigParser()
config.read('settings.conf')

# Engine is the core interface to the database
dbconnect = config["MYSQL"]["SQLALCHEMY_DATABASE_URI"]
engine = create_engine(dbconnect, echo=True)

# Create a database session, bind to the engine and prepare to use
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Base class for declaring tables
Base = declarative_base()

# Define tables
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    username = Column(String(50), unique=True)
 
    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', username='%s')>" % (self.name, self.fullname, self.username)

# Define tables
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates = "addresses")

    
    # def __repr__(self):
    #     return "<Addresses(email='%s', facebook='%s', user_id='%s')>" % (self.email, self.facebook, self.user_id)


User.addresses = relationship("Address", order_by = Address.id, back_populates = "user")


# Create the tables in the database
Base.metadata.create_all(engine)

# Add data to the tables
ed_user = User(name='ed', fullname='Ed Jones', username='edjones')
ed_user.addresses = [Address(address = "ed@gmails.com", type = "email"), Address(address = "bigedfb", type = "facebook")]

wendy =User(name='wendy', fullname='Wendy Williams', username='windy')
wendy.addresses = [Address(address = "wendy@hotmails.com", type = "email")]

session.add(ed_user)
session.add(wendy)

# Add multiple rows to the table
session.add_all([
    User(name='mary', fullname='Mary Contrary', username='mary'),
    User(name='fred', fullname='Fred Flintstone', username='freddy')])

# Commit actually adds the data
session.commit()

