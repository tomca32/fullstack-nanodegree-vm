from flask import render_template, request, redirect, url_for, flash

from app.decorators import with_category
from .. import app
from ..services import create_category, category_exists, get_items_by_category_id


@app.route('/category/new', methods=['GET'])
def new_category_form():
    return render_template('category_new.html')


@app.route('/category/new', methods=['POST'])
def new_category():
    if category_exists(request.form['name']):
        flash('Error: Category with that name already exists.')
        return redirect(url_for('new_category_form'))
    create_category(request.form['name'])
    return redirect(url_for('root'))


@app.route('/category/<string:category_name>/')
@with_category
def get_category(category):
    items = get_items_by_category_id(category.id)
    return render_template('category.html', category=category, items=items)
