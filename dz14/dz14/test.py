from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dz14.db', connect_args={'check_same_thread': False}) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
DeclarativeBase = declarative_base()
DeclarativeBase.metadata.create_all(engine)