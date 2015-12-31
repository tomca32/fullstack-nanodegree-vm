from flask import render_template, request, redirect, url_for, flash
from .. import app
from .. import session
from ..models import Category
from ..services import itemExists, createItem

@app.route('/item/new', methods = ['GET'])
def newItemForm():
  categories = session.query(Category).all()
  return render_template('item_new.html', categories = categories)

@app.route('/item/new', methods = ['POST'])
def newItem():
  if itemExists(request.form['name']):
    flash('Error: Item with that name already exists')
    return redirect(url_for('newItemForm'))
  createItem(request.form['name'], request.form['description'], request.form['category'])
  return redirect(url_for('root'))
