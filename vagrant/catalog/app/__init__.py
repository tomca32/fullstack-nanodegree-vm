from flask import Flask, render_template, request, Response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.security_service import generate_csrf_token

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


@app.before_request
def create_csrf_token():
    if 'logged_in' not in login_session and request.endpoint not in ('gconnect', 'static'):
        login_session['state'] = generate_csrf_token()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(401)
def not_authorized(error):
    return Response('You need to be logged in to perform that action', 401)
