from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from datetime import datetime  

class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    finished = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    assigned_to = relationship("Users", back_populates="tasks")

    def update_status(self, finished: bool):
        self.finished = finished
        if finished :
            self.finished_at = datetime.now()
        else : 
            self.finished_at = None

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    tasks = relationship("Tasks", back_populates="assigned_to")