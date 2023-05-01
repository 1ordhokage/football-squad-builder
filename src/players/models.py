from sqlalchemy import Column, Integer, String

from src.database.database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    photo_url = Column(String)
    nationality = Column(String)
    flag_url = Column(String)
    club = Column(String)
    club_logo_url = Column(String)
    value = Column(String)
    foot = Column(String)
    height = Column(String)
    weight = Column(String)
    kit_number = Column(Integer)
