from flask import render_template, request, redirect, url_for, flash
from .. import app
from .. import session
from ..models import Category
from ..services import item_exists, create_item


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
