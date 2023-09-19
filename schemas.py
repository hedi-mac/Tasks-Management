from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Task(TaskBase):
    finished: Optional[bool] = None
    created_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
