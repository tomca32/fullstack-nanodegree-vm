from flask import render_template, request, redirect, url_for, flash, jsonify, Response
import xml.etree.ElementTree as ET

from app.decorators import with_category, logged_in
from .. import app
from ..services import create_category, category_exists, get_items_by_category_id


@app.route('/category/new', methods=['GET'])
@logged_in
def new_category_form():
    return render_template('category_new.html')


@app.route('/category/new', methods=['POST'])
@logged_in
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


@app.route('/category/<string:category_name>/json/')
@with_category
def get_category_json(category):
    items = get_items_by_category_id(category.id)
    return jsonify(category.serialize, **{'items': [i.serialize for i in items]})


@app.route('/category/<string:category_name>/xml/')
@with_category
def get_category_xml(category):
    category_xml = category.to_xml_element

    items = ET.Element('items')
    items.extend([i.to_xml_element for i in get_items_by_category_id(category.id)])

    category_xml.append(items)
    return Response(ET.tostring(category_xml), mimetype='text/xml')
