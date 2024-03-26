from sqlalchemy import create_engine, Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@postgresdb/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class PlatformEnum(PyEnum):
    PC = "PC"
    Mobile = "Mobile"
    PlayStation = "PlayStation"

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    platform = Column(Enum(PlatformEnum), index=True)
    main_actions = Column(Text)

def create_db_tables():
    Base.metadata.create_all(bind=engine)

create_db_tables()








