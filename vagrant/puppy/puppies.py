import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelters'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(250))
	state = Column(String(80))
	zipCode = Column(String(5))
	website = Column(String(150))


class Puppy(Base):
	__tablename__ = 'puppies'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	dateOfBirth = Column(Date)
	breed = Column(String(80))
	gender = Column(String(1), nullable = False)
	weight = Column(Float)
	picture = Column(String(250))
	shelter_id = Column(Integer, ForeignKey('shelters.id'))
	shelter = relationship(Shelter)



engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)