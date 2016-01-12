import xml.etree.ElementTree as ET

from sqlalchemy import Column, Integer, String

from .. import Base


class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @property
    def to_xml_element(self):
        category = ET.Element('category')

        id_xml = ET.Element('id')
        id_xml.text = str(self.id)

        name = ET.Element('name')
        name.text = self.name

        category.extend([id_xml, name])
        return category
