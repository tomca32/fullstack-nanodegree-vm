from flask import render_template, jsonify

from app.services import get_items_by_category_id
from .. import app
from .. import session
from ..models import Category, Item


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
