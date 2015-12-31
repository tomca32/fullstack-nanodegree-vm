from flask import render_template
from .. import app
from .. import session
from ..models import Category, Item

@app.route('/')
def root():
  categories = session.query(Category).all()
  items = session.query(Item).all()
  return render_template('root.html', categories = categories, items = items)
