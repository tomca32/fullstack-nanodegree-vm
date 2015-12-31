from flask import render_template
from .. import app

@app.route('/category/new')
def newCategory():
  return render_template('category_new.html')
