from ..models import Category
from .. import session

def categoryExists(name):
  return session.query(Category).filter_by(name = name).count() > 0

def createCategory(name):
  newCategory = Category(name = name)
  session.add(newCategory)
  session.commit()
