from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

r1 = Restaurant(name = 'Pizza Palace')
r2 = Restaurant(name = 'Steak Palace')

session.add(r1)
session.add(r2)
session.commit()

i1 = MenuItem(name = 'Cheese Pizza', description = 'Pizza with cheese', price = '$8.99', restaurant = r1)
i2 = MenuItem(name = 'Sausage Pizza', description = 'Pizza with Sausage', price = '$8.99', restaurant = r1)
i3 = MenuItem(name = 'Sausage and Cheese Pizza', description = 'Pizza with Sausage and Cheese', price = '$12.99', restaurant = r1)

session.add(i1)
session.add(i2)
session.add(i3)

session.commit()
