import xml.etree.ElementTree as ET
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, func
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
    image_url = Column(String(250))
    created_at = Column(DateTime, default=func.now())

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'category': self.category.name,
            'category_id': self.category_id,
            'image_url': self.image_url
        }

    @property
    def to_xml_element(self):
        id = ET.Element('id')
        id.text = str(self.id)

        name = ET.Element('name')
        name.text = self.name

        description = ET.Element('description')
        description.text = self.description

        category = ET.Element('category')
        category.text = self.category.name

        category_id = ET.Element('category_id')
        category_id.text = str(self.category_id)

        image_url = ET.Element('image_url')
        image_url.text = self.image_url

        item = ET.Element('item')
        item.extend([id, name, description, category, category_id, image_url])

        return item
