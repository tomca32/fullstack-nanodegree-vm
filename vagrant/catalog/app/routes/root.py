from flask import render_template
from .. import app
from .. import session
from ..models import Category

@app.route('/')
def root():
  categories = session.query(Category).all()
  return render_template('root.html', categories = categories)
