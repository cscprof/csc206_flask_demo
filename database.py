# Example from https://docs.sqlalchemy.org/en/14/orm/tutorial.html
# Example from https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_related_objects.htm

# import the framwework
from enum import unique
import os
from flask import Flask, render_template, request

from database.db_connector import DbConnector
from database.demo_db import School, Major, Association

# Create the application instance
app = Flask(__name__)

@app.route('/')
def index():

    db = DbConnector()
    session = db.session

    # schools = session.query(School).filter(Major.schools.any()).all()
    schools = session.query(School, Major, Association).join(School.majors).join(Major)

    for record in schools:
        print(record)

    return render_template('database.html', schools=schools)

if __name__ == '__main__':
    app.run(debug=True)