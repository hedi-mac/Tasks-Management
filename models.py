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

    def mark_as_finished(self):
        self.finished = True
        self.finished_at = datetime.now()