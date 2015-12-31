from ..models import Category
from .. import session


def category_exists(name):
    return session.query(Category).filter_by(name=name).count() > 0


def create_category(name):
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()


def get_category_by_name(name):
    return session.query(Category).filter_by(name=name).one()
