#!/usr/bin/env python3
"""
this is a basic flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world
    """
    return render_template('0-index.html')
