from flask import render_template, request, redirect, url_for, flash
from .. import app
from .. import session
from ..services import createCategory, categoryExists

@app.route('/category/new', methods = ['GET'])
def newCategoryForm():
  return render_template('category_new.html')

@app.route('/category/new', methods = ['POST'])
def newCategory():
  if categoryExists(request.form['name']):
    flash('Error: Category with that name already exists.')
    return redirect(url_for('newCategoryForm'))
  createCategory(request.form['name'])
  return redirect(url_for('root'))
