from urlparse import urlparse

from flask import render_template, request, redirect, url_for, flash, jsonify, Response
import xml.etree.ElementTree as ET
from app.decorators import with_item, provide_query_args, logged_in, with_item_by_id, check_csrf
from .. import app
from .. import session
from ..models import Category
from ..services import item_exists, create_item, update_item, drop_item


@app.route('/item/new', methods=['GET'])
@logged_in
@provide_query_args
def new_item_form(default_name='', default_description='', default_category_name='', default_image_url=''):
    """
    Displays a form for new item and also displays previous attempted fields if the form was invalid
    :param default_name: Default name for the new item - displayed from the previous attempt if it failed
    :param default_description: Default description - displayed from the previous attempt if it failed
    :param default_category_name: Default category - displayed from the previous attempt if it failed
    :param default_image_url: Default image URL - displayed from the previous attempt if it failed
    :return: rendered template item_new.html
    """
    categories = session.query(Category).all()
    return render_template('item_new.html', categories=categories, default_name=default_name,
                           default_description=default_description,
                           default_category_name=default_category_name, default_image_url=default_image_url)


@app.route('/item/new', methods=['POST'])
@logged_in
def new_item():
    name = request.form['name'].strip()
    if item_exists(name):
        flash('Error: Item with that name already exists')
        return redirect(retry_new_item(request.form))
    if name == '':
        flash('Error: Item must have a name')
        return redirect(retry_new_item(request.form))
    create_item(request.form['name'], request.form['description'].strip(), request.form['category'], request.form['image_url'])
    return redirect(url_for('root'))


@app.route('/category/<string:category_name>/item/<string:item_name>/')
@with_item
def get_item(item):
    return render_template('item.html', item=item)


@app.route('/item/<string:item_id>/')
@with_item_by_id
def get_item_by_id(item):
    return redirect((url_for('get_item', item_name=item.name, category_name=item.category.name)))


@app.route('/category/<string:category_name>/item/<string:item_name>/json/')
@with_item
def get_item_json(item):
    return jsonify(item.serialize)


@app.route('/category/<string:category_name>/item/<string:item_name>/xml/')
@with_item
def get_item_xml(item):
    return Response(ET.tostring(item.to_xml_element), mimetype='text/xml')


@app.route('/item/<string:item_id>/json/')
@with_item_by_id
def get_item_by_id_json(item):
    return redirect((url_for('get_item_json', item_name=item.name, category_name=item.category.name)))


@app.route('/item/<string:item_id>/xml/')
@with_item_by_id
def get_item_by_id_xml(item):
    return redirect((url_for('get_item_xml', item_name=item.name, category_name=item.category.name)))


@app.route('/category/<string:category_name>/item/<string:item_name>/edit', methods=['GET'])
@logged_in
@with_item
def edit_item_form(item):
    categories = session.query(Category).all()
    return render_template('item_edit.html', item=item, categories=categories)


@app.route('/item/<int:item_id>/edit', methods=['POST', 'PUT'])
@logged_in
def edit_item(item_id):
    update_item(item_id, request.form['name'], request.form['description'], request.form['category'])
    return redirect(url_for('get_item', category_name=request.form['category'], item_name=request.form['name']))


@app.route('/category/<string:category_name>/item/<string:item_name>/delete', methods=['GET'])
@logged_in
@with_item
def delete_item_form(item):
    return render_template('item_delete.html', item=item)


@app.route('/item/<int:item_id>/delete', methods=['POST', 'DELETE'])
@logged_in
@check_csrf
def delete_item(item_id):
    drop_item(item_id)
    return redirect(url_for('root'))


def retry_new_item(form):
    return url_for('new_item_form', default_name=form['name'], default_description=form['description'],
                   default_category_name=form['category'], default_image_url=form['image_url'])
