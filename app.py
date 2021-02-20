import flask
from flask import request, make_response, jsonify, redirect

from datetime import datetime

app = flask.Flask(__name__)

default_user = {'name':'default_user', 'bio':'default_bio', 'color-scheme':'default'}

@app.route('/')
def base_page():
    return flask.render_template("base.html", user=default_user, page_title="Test")

@app.route("/info")
def info_page():
    return flask.render_template("info.html", user=default_user, page_title="Information")

@app.route("/profile")
def profile():
    return flask.render_template("profile.html", user=default_user, page_title="Profile")

@app.route("/dashboard")
def dashboard():
    return flask.render_template("dashboard.html", user=default_user, page_title="Dashboard")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)