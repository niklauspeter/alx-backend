#!/usr/bin/env python3
"""
Use Get locale fucnction with babel.localeselector decorator 
use request.accept_languages to determine best match with
supported languages
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
     use function to determine the
     best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    render to hello world template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
