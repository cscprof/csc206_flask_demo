# import the framwework
import os
from flask import Flask, render_template, request
from flask_mail import Message, Mail
import flask_bootstrap
import configparser
config = configparser.ConfigParser()
config.read('settings.conf')


# Create the application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = config["DEFAULT"]["SECRET_KEY"]
app.config['MAIL_SERVER'] = config["EMAIL"]["MAIL_SERVER"]
app.config['MAIL_PORT'] = config["EMAIL"]["MAIL_PORT"]
app.config['MAIL_USE_TLS'] = config["EMAIL"]["MAIL_USE_TLS"]
app.config['MAIL_USERNAME'] = config["EMAIL"]["MAIL_USERNAME"]
app.config['MAIL_PASSWORD'] = config["EMAIL"]["MAIL_PASSWORD"]

mail = Mail(app)

def send_email(to_addr, subject, from_addr, template, **kwargs):
    print(from_addr)
    msg = Message(subject, sender = from_addr, recipients = to_addr)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


@app.route('/', methods = ['GET'])
def index():
    return render_template('email_create.html')


@app.route('/', methods = ['POST'])
def sendemail():

    # Get the form values
    message = {"name": [], "email": [], "subject":[], "message":[]}
    message['name'].append(request.form.get('name'))
    message['email'].append(request.form.get('email'))
    message['subject'].append(request.form.get('subject'))
    message['message'].append(request.form.get('message'))

    send_email(message["email"], message["subject"][0], config["EMAIL"]["MAIL_FROM"], "mail/email_sent", message=message)
    print(message)

    return render_template('email_create.html')    


if __name__ == '__main__':
    app.run(debug=True)