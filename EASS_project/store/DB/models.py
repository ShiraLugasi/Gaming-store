from sqlalchemy import Column, Integer, String, Text, Enum
from DB import Base, PlatformEnum

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    platform = Column(Enum(PlatformEnum), index=True)
    main_actions = Column(Text)








