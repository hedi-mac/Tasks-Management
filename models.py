from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func
from datetime import datetime  

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    finished = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)

    def update_status(self, finished: bool):
        self.finished = finished
        if finished :
            self.finished_at = datetime.now()
        else : 
            self.finished_at = None

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)