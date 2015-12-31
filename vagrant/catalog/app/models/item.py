from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from category import Category
from .. import Base


class Item(Base):
    __tablename__ = 'item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(Text())
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
