import enum
from sqlalchemy import Enum, Column, String

from app.data.database import Base


class Task(Base):
    __tablename__ = 'Task'

    id = Column(String, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False)
