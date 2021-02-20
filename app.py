import flask
from flask import request, make_response, jsonify, redirect

from datetime import datetime

app = flask.Flask(__name__)

default_user = {"color-scheme":"default"}

@app.route('/')
def base_page():
    return flask.render_template("base.html", user=default_user, page_title="Test")

@app.route("/info")
def info_page():
    return flask.render_template("info.html", user=default_user, page_title="Information")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)