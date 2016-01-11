import random
import string

from flask import Flask, render_template, request
from flask import session as login_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')

# Database config
Base = declarative_base()

import models

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

import routes


def generate_csrf_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in xrange(32))


@app.before_request
def create_csrf_token():
    if 'logged_in' not in login_session and request.endpoint not in ('gconnect', 'static'):
        login_session['state'] = generate_csrf_token()
        print login_session['state']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
