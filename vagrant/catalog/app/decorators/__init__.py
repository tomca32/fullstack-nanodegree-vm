from flask import render_template
from sqlalchemy.orm.exc import NoResultFound

from app.services import get_category_by_name, get_item_by_name_and_category_id


def with_category(f):
    """
    This decorator provides a Category for the decorated view function
    :param f: view function or route being decorated
    :return: a decorator providing the category for the view function or rendering 404 if Category doesn't exist
    """
    def decorator(category_name, **kwargs):
        try:
            category = get_category_by_name(category_name)
        except NoResultFound:
            return render_template('404.html', message="Category '{0}' does not exist.".format(category_name))
        return f(category=category, **kwargs)

    decorator.__name__ = f.__name__ # decorator gets the same name as the decorated function to preserve routing
    return decorator


def with_item(f):
    """
    This decorator provides an Item for the decorated view function
    :param f: view function or route being decorated
    :return: decorated providing the Item for the view function or rendering 404 if Category or Item don't exist
    """
    def decorator(category_name, item_name):
        try:
            category = get_category_by_name(category_name)
        except NoResultFound:
            return render_template('404.html', message="Category '{0}' does not exist.".format(category_name))

        try:
            item = get_item_by_name_and_category_id(item_name, category.id)
        except NoResultFound:
            return render_template('404.html', message="Item '{0}' does not exist in category {1].".format(item_name,
                                                                                                           category.name))
        return f(item=item)
    decorator.__name__ = f.__name__ # decorator gets the same name as the decorated function to preserve routing
    return decorator
