from ..models import Item, Category
from .. import session


def item_exists(name):
    return session.query(Item).filter_by(name=name).count() > 0


def create_item(name, description, category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    new_item = Item(name=name, description=description, category=category)
    session.add(new_item)
    session.commit()
