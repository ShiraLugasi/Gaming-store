from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    platform = Column(String, index=True)
    edition = Column(String, index=True)
    price = Column(Numeric(10, 2))
