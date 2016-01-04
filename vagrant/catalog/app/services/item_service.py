from app.services import get_category_by_name
from ..models import Item, Category
from .. import session


def get_item_by_id(id):
    return session.query(Item).filter_by(id=id).one()


def item_exists(name):
    return session.query(Item).filter_by(name=name).count() > 0


def create_item(name, description, category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    new_item = Item(name=name, description=description, category=category)
    session.add(new_item)
    session.commit()


def update_item(item_id, name, description, category_name):
    item = get_item_by_id(item_id)
    category = get_category_by_name(category_name)
    item.name = name
    item.description = description
    item.category = category
    session.add(item)
    session.commit()


def get_items_by_category_id(category_id):
    return session.query(Item).filter_by(category_id=category_id).all()


def get_item_by_name_and_category_id(item_name, category_id):
    return session.query(Item).filter_by(name=item_name, category_id=category_id).one()


def drop_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    session.delete(item)
    session.commit()
