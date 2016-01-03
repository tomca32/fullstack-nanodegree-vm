from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.orm.exc import NoResultFound

from .. import app
from .. import session
from ..models import Category
from ..services import item_exists, create_item, get_category_by_name, get_item_by_name_and_category_id, update_item


@app.route('/item/new', methods=['GET'])
def new_item_form():
    categories = session.query(Category).all()
    return render_template('item_new.html', categories=categories)


@app.route('/item/new', methods=['POST'])
def new_item():
    if item_exists(request.form['name']):
        flash('Error: Item with that name already exists')
        return redirect(url_for('new_item_form'))
    create_item(request.form['name'], request.form['description'], request.form['category'])
    return redirect(url_for('root'))


@app.route('/category/<string:category_name>/item/<string:item_name>/')
def get_item(category_name, item_name):
    try:
        category = get_category_by_name(category_name)
    except NoResultFound:
        return render_template('404.html', message="Category '{0}' does not exist.".format(category_name))
    try:
        item = get_item_by_name_and_category_id(item_name, category.id)
    except NoResultFound:
        return render_template('404.html',
                               message="Item '{0}' does not exist in category {1].".format(item_name, category_name))
    return render_template('item.html', item=item)


@app.route('/category/<string:category_name>/item/<string:item_name>/edit', methods=['GET'])
def edit_item_form(category_name, item_name):
    try:
        category = get_category_by_name(category_name)
    except NoResultFound:
        return render_template('404.html', message="Category '{0}' does not exist.".format(category_name))
    try:
        item = get_item_by_name_and_category_id(item_name, category.id)
    except NoResultFound:
        return render_template('404.html',
                               message="Item '{0}' does not exist in category {1].".format(item_name, category_name))
    categories = session.query(Category).all()
    return render_template('item_edit.html', item=item, categories=categories)


@app.route('/item/<int:item_id>/edit', methods=['POST', 'PUT'])
def edit_item(item_id):
    update_item(item_id, request.form['name'], request.form['description'], request.form['category'])
    return redirect(url_for('get_item', category_name=request.form['category'], item_name=request.form['name']))
