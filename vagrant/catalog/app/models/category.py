from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .. import Base


class Category(Base):
  __tablename__ = 'category'
  name = Column(String(80), nullable = False)
  id = Column(Integer, primary_key = True)
