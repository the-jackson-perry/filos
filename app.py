import flask
from flask import request, make_response, jsonify, redirect

from datetime import datetime

app = flask.Flask(__name__)

@approute('/')
def base_page():
    return flask.render_template("base.html", page_title="Test")
