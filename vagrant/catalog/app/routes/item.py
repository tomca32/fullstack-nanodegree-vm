from flask import render_template, request, redirect, url_for, flash

from app.decorators import with_item
from .. import app
from .. import session
from ..models import Category
from ..services import item_exists, create_item, update_item


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
@with_item
def get_item(item):
    return render_template('item.html', item=item)


@app.route('/category/<string:category_name>/item/<string:item_name>/edit', methods=['GET'])
@with_item
def edit_item_form(item):
    categories = session.query(Category).all()
    return render_template('item_edit.html', item=item, categories=categories)


@app.route('/item/<int:item_id>/edit', methods=['POST', 'PUT'])
def edit_item(item_id):
    update_item(item_id, request.form['name'], request.form['description'], request.form['category'])
    return redirect(url_for('get_item', category_name=request.form['category'], item_name=request.form['name']))
