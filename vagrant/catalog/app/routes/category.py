from flask import render_template, request, redirect, url_for
from .. import app
from .. import session
from ..models import Category

@app.route('/category/new', methods = ['GET'])
def newCategoryForm():
  return render_template('category_new.html')

@app.route('/category/new', methods = ['POST'])
def newCategory():
  newCategory = Category(name = request.form['name'])
  session.add(newCategory)
  session.commit()
  return redirect(url_for('root'))