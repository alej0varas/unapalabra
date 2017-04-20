from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()
 

class Lema(Base):
    __tablename__ = 'lema'
    id = Column(Integer, primary_key=True)

    rae_id = Column(String(10))
    text = Column(Text())

engine = create_engine('sqlite:///database.db')
 
Base.metadata.create_all(engine)
