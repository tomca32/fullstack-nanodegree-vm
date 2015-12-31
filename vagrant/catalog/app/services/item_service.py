from ..models import Item, Category
from .. import session

def itemExists(name):
  return session.query(Item).filter_by(name = name).count() > 0

def createItem(name, description, categoryName):
  category = session.query(Category).filter_by(name = categoryName).one()
  newItem = Item(name = name, description = description, category = category)
  session.add(newItem)
  session.commit()
