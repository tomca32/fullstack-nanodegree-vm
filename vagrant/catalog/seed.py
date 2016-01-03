from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base

from app.models import Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Category).delete()
session.query(Item).delete()
session.commit()

starfighters_category = Category(name='Starfighters')
capitals_category = Category(name='Capital Ships')

session.add(starfighters_category)
session.add(capitals_category)
session.commit()

x_wing = Item(name='X-Wing',
              description='The Incom T-65 X-wing starfighter was the primary all-purpose starfighter of the Rebel Alliance and its successor governments. Known for its versatility and exceptional combat performance, it was a favorite with Rebel and New Republic pilots.',
              category=starfighters_category)

y_wing = Item(name='Y-Wing',
              description='The BTL Y-wing starfighter was a fighter-bomber built by Koensayr Manufacturing. First used during the Clone Wars, during the Galactic Civil War it was a mainstay of the Alliance Starfighter Corps. It was often used as an assault bomber to attack enemy capital ships directly in conjunction with the later B-wing starfighters.',
              category=starfighters_category)

tie_fighter = Item(name='TIE Fighter',
                   description='The TIE/LN starfighter, commonly known as the TIE fighter, was the signature starfighter of the Galactic Empire, with a later model being used by the First Order. They were instantly recognizable from the roar of their engines and carried locator beacons enabling them to be found by the Empire.',
                   category=starfighters_category)

star_destroyer = Item(name='Star Destroyer',
                      description='The Imperial-class Star Destroyer was a type of Star Destroyer widely used by the Galactic Empire and the Imperial Remnant. There were two sub-classes of the line: the Imperial I-class Star Destroyer (also known as Imperator-class), and the Imperial II-class Star Destroyer.',
                      category=capitals_category)

mc_80 = Item(name='MC80 Liberty type Star Cruiser',
                      description='The MC80 Liberty type Star Cruiser was an early type of Mon Calamari Star Cruiser put into service for the Rebel Alliance during the Galactic Civil War.',
                      category=capitals_category)

mc_80_home_one = Item(name='MC80 Home One type Star Cruiser',
                      description='The MC80 Home One type Star Cruiser, also known as the MC80 Command Cruiser was one of the several MC80 Star Cruiser designs built by the Mon Calamari. Originally fielded before the Galactic Civil War as civilian vessels, they were modified by the Rebel Alliance, and served in command ship and battleship roles in the Alliance Fleet.',
                      category=capitals_category)

victory = Item(name='Victory I-class Star Destroyer',
                      description='The Victory I-class Star Destroyer, also known as the Victory I-class Destroyer and Victoria I-class Star Destroyer, was a warship designed for planetary defense, planetary assault, ground troop support, and ship-to-ship combat. It was used by the Galactic Republic during the mid-Clone Wars, the Galactic Empire and the Corporate Sector during the Galactic Civil War and the Confederation during the Second Galactic Civil War.',
                      category=capitals_category)



session.add(x_wing)
session.add(y_wing)
session.add(tie_fighter)
session.add(star_destroyer)
session.add(mc_80)
session.add(mc_80_home_one)
session.add(victory)
session.commit()
