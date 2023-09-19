from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
