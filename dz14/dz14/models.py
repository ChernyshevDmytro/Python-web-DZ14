from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base() 

class Person(Base):
    __tablename__ = "person"    
    id = Column(Integer, primary_key=True)
    author_name = Column(String(50), nullable=False)
    additional_info = Column(String(50), nullable=True)
    keywords = relationship("Keywords", cascade="all, delete", backref="person")
    quotes = relationship("Quotes", cascade="all, delete", backref="person")
    

class Keywords(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50))
    author_id = Column(Integer, ForeignKey('person.id', ondelete="CASCADE")) 

class Quotes(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    quote = Column(String(50))
    author_id = Column(Integer, ForeignKey('person.id', ondelete="CASCADE"))     