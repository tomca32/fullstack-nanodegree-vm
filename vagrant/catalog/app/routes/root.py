from flask import render_template, jsonify, Response

from app.services import get_items_by_category_id
from .. import app
from .. import session
from ..models import Category, Item
import xml.etree.ElementTree as ET


@app.route('/')
def root():
    categories = session.query(Category).all()
    items = session.query(Item).all()
    return render_template('root.html', categories=categories, items=items)


@app.route('/json/')
def root_json():
    categories = session.query(Category).all()
    res = {'categories': [dict(c.serialize, **{'items': [i.serialize for i in get_items_by_category_id(c.id)]}) for c in categories]}
    return jsonify(res)


@app.route('/xml/')
def root_xml():
    categories = session.query(Category).all()

    categories_xml = ET.Element('categories')

    for c in categories:
        category_xml = c.to_xml_element

        items = ET.Element('items')
        items.extend([i.to_xml_element for i in get_items_by_category_id(c.id)])

        category_xml.append(items)
        categories_xml.append(category_xml)

    return Response(ET.tostring(categories_xml), mimetype='text/xml')
