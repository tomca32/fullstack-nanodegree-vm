from ..models import Item, Category
from .. import session


def item_exists(name):
    return session.query(Item).filter_by(name=name).count() > 0


def create_item(name, description, category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    new_item = Item(name=name, description=description, category=category)
    session.add(new_item)
    session.commit()


def get_items_by_category_id(category_id):
    return session.query(Item).filter_by(category_id=category_id).all()


def get_item_by_name_and_category_id(item_name, category_id):
    return session.query(Item).filter_by(name=item_name, category_id=category_id).one()
