import flask
from flask import request, make_response, jsonify, redirect
import random

from datetime import datetime

app = flask.Flask(__name__)

quote_list = ['You are awesome!', 'Have a great day!', "Gimme a smile :)", "Never Give Up!"]

default_user = {'name':'default_user', 'bio':'default_bio', 'color-scheme':'default', 'friends':['friend1', 'friend2', 'friend3']}

@app.route('/base')
def base_page():
    return flask.render_template("base.html", user=default_user, page_title="Test")

@app.route("/info")
def info_page():
    return flask.render_template("info.html", user=default_user, page_title="Information")

@app.route("/profile")
def profile():
    return flask.render_template("profile.html", user=default_user, page_title="Profile", friends=default_user['friends'])

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return flask.render_template("dashboard.html", user=default_user, page_title="Dashboard", quote=quote_list[random.randint(0,len(quote_list)-1)])

@app.route("/messages")
def messages():
    return flask.render_template("messages.html", user=default_user, page_title="Messages")

@app.route("/friends")
def friends():
    return flask.render_template("friends.html", user=default_user, page_title="Friends", friends=default_user['friends'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)