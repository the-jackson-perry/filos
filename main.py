from flask import Flask, render_template, request
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
import datetime

import random
import user_database

app = Flask(__name__)

quote_list = ['You are awesome!', 'Have a great day!', "Gimme a smile :)", "Never Give Up!"]

default_user = {'name':'default_user', 'bio':'default_bio', 'color-scheme':'default', 'friends':['friend1', 'friend2', 'friend3']}

firebase_request_adapter = requests.Request()
@app.route('/')
def root():
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None

    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

    return render_template(
        'login.html',
        user_data=claims, error_message=error_message, times=times)


@app.route('/base')
def base_page():
    return render_template("base.html", user=default_user, page_title="Test")

@app.route("/info")
def info_page():
    return render_template("info.html", user=default_user, page_title="Information")

@app.route("/profile")
def profile():
    return render_template("profile.html", user=default_user, page_title="Profile", friends=default_user['friends'])

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user=default_user, page_title="Dashboard", quote=quote_list[random.randint(0,len(quote_list)-1)])

@app.route("/messages")
def messages():
    return render_template("messages.html", user=default_user, page_title="Messages")

@app.route("/friends")
def friends():
    return render_template("friends.html", user=default_user, page_title="Friends", friends=default_user['friends'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)