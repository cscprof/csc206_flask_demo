# REsources - https://docs.sqlalchemy.org/en/14/tutorial/data_select.html


from flask import Flask, jsonify, Response
import configparser
from sqlalchemy import MetaData, create_engine, select
from sqlalchemy import Table, Column, Integer, String, Float

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
config = configparser.ConfigParser()
config.read('settings.conf')

app = Flask(__name__)
# Read the secret key - required for sessions to work
app.secret_key = config["DEFAULT"]["SECRET_KEY"]

metadata_obj = MetaData()

# Setup the table
athlete_table = Table(
    "athletes",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(50)),
    Column('currentrank', Integer),
    Column('prevyearrank', Integer),
    Column('sport', String(50)),
    Column('year', Integer),
    Column('earnings', Float)
)

# Connect to database
engine = create_engine(config["MYSQL"]["SQLALCHEMY_DATABASE_URI"],echo=True)

@app.route('/')
def index():
    return "<h2>Athlete Functions. Try /athletes or /athletes/id</h2>"


#
# Get all baseball athletes data 
#
@app.route('/athletes', methods=['GET'])
def allAthletes():
    # stmt = select(athlete_table).where(athlete_table.c.sport == 'football')
    stmt = select(athlete_table)
    with engine.connect() as conn:
        print(conn.execute(stmt).all())        
        results = conn.execute(stmt).all()

    athlete_list = [r._asdict() for r in results]
    athlete_json = jsonify(athlete_list)
    return athlete_json

#
# Get data for a specific athlete
#
@app.route('/athletes/<id>', methods=['GET'])
def athlete(id):
    print(id)
    stmt = select(athlete_table).where(athlete_table.c.id == id)
    with engine.connect() as conn:
        print(conn.execute(stmt).all())        
        results = conn.execute(stmt).all()

    athlete_list = [r._asdict() for r in results]

    return jsonify(athlete_list)


if __name__ == '__main__':
    app.debug = True
    app.run()
