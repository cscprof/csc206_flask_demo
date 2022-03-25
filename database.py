# Example from https://docs.sqlalchemy.org/en/14/orm/tutorial.html
# Example from https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_related_objects.htm

# import the framwework
from enum import unique
import os
from flask import Flask, render_template, request

# Import the database model and connection information
import user_addreses as db

# Create the application instance
app = Flask(__name__)


@app.route('/')
def index():
    people = db.session.query(db.User).all()
    return render_template('database.html', people=people)


if __name__ == '__main__':
    app.run(debug=True)