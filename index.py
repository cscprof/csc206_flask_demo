from flask import Flask, render_template, request, make_response, session, flash
from flask_bootstrap import Bootstrap
from flask_session import Session
import configparser

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
config = configparser.ConfigParser()
config.read('settings.conf')

app = Flask(__name__)
# Read the secret key - required for sessions to work
app.secret_key = config["DEFAULT"]["SECRET_KEY"]

# Read session configuration values
app.config["SESSION_PERMANENT"] = config["SESSION"]["SESSION_PERMANENT"]
app.config["SESSION_TYPE"] = config["SESSION"]["SESSION_TYPE"]

# Init flask_bootstrap
Bootstrap(app)

# Init session functions
Session(app)

@app.route('/', methods=['GET'])
def index():

    session["name"] = "Scott"
    session["employer"] = "Geneva College"

    flash(session["name"])
    flash(session["employer"])

    print(app.config["SECRET_KEY"])

    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_form():

   upperlimit = request.form['upperlimit']
   return '<h1>Upper limit: {}</h1>'.format(upperlimit)


if __name__ == '__main__':
    app.debug = True
    app.run()
