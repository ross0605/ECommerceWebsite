from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from flask import request

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


###################################################################
class Clothing(Base):
	""""""
	__tablename__ = "Pieces"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	description = Column(String)
	price = Column(Integer)
	image = Column(String)
	image2 = Column(String)
	image3 = Column(String)
	small = Column(Integer)
	medium = Column(Integer)
	large = Column(Integer)
	ext = Column(String)

	
	def __init__(self, name, description, price, image, image2, image3, small, medium, large, ext):
		""""""

		self.name = name
		self.description = description
		self.price = price
		self.image = image
		self.image2 = image2
		self.image3 = image3
		self.small = small
		self.medium = medium
		self.large = large
		self.ext = ext

	def __repr__(self):
		return "<Pieces(name='%s', description='%s', price='%i', image=%s'', image2='%s', image3=%s'', small='%i', medium='%i', large='%i', ext='%s'" % (self.name, self.description, self.price, self.image, self.image2, self.image3, self.small, self.medium, self.large, self.ext)


#Create Tables
Base.metadata.create_all(engine)
