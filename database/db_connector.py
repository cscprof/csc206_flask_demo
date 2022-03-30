from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import configparser

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
# config = configparser.ConfigParser()
# config.read('settings.conf')

# # Engine is the core interface to the database
# dbconnect = config["MYSQL"]["SQLALCHEMY_DATABASE_URI"]
# engine = create_engine(dbconnect, echo=True)


class DbConnector:   

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.conf')

        # Engine is the core interface to the database
        dbconnect = self.config["MYSQL"]["SQLALCHEMY_DATABASE_URI"]
        engine = create_engine(dbconnect, echo=True)

        # Create a databsae session, bind to the engine and prepare to use
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def Session(self):
        return self.session