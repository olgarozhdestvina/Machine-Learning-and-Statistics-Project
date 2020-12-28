#!flask/bin/python

"""
Project assessment
Machine Learning and Statistics Module - GMIT 2020
Submitted by: Olga Rozhdestvina (Student No: G00387844)
Lecturer: Ian McLoughlin
"""

# MAIN FLASK SERVER.

from flask import Flask, render_template
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError

# Flask app.
app = Flask(__name__, static_folder="static",
            template_folder="templates")

# Main page.
@app.route('/')
def home():
    return render_template("index.html")

# Error handlers.
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Bad request!', 400


@app.errorhandler(NotFound)
def handle_bad_request(e):
    return 'Page is not found!', 404


@app.errorhandler(MethodNotAllowed)
def handle_bad_request(e):
    return 'Method is not allowed!', 405


@app.errorhandler(InternalServerError)
def handle_bad_request(e):
    return 'Internal server error!', 500

if __name__ == '__main__':
    app.run(debug=True)