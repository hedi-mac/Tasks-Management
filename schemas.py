from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Task(TaskBase):
    finished: Optional[bool] = None
    created_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

class User(BaseModel):
    user_name: str
    email: str
    password: str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    user_name: str
    email: str
    tasks: List[Task] = []
    class Config():
        orm_mode = True

class ShowTask(TaskBase):
    class Config():
        orm_mode = True
    finished: Optional[bool] = None
    finished_at: Optional[datetime] = None
    assigned_to: Optional[ShowUser]

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    

