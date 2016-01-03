from flask import Flask, render_template
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


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
