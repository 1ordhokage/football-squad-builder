from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String

from src.database.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
