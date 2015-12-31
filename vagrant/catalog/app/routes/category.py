from flask import render_template, request, redirect, url_for, flash
from .. import app
from .. import session
from ..models import Category

@app.route('/category/new', methods = ['GET'])
def newCategoryForm():
  return render_template('category_new.html')

@app.route('/category/new', methods = ['POST'])
def newCategory():
  existingCategories = session.query(Category).filter_by(name = request.form['name']).count()
  if existingCategories > 0:
    flash('Error: Category with that name already exists.')
    return redirect(url_for('newCategoryForm'))

  newCategory = Category(name = request.form['name'])
  session.add(newCategory)
  session.commit()
  return redirect(url_for('root'))