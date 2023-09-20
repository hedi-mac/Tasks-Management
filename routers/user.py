from typing import List, Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import User, ShowUser
import models
import database
from hashing import Hash

router = APIRouter(
    prefix="/users",
    tags=['USERS']
)

db_dependency = Annotated[Session, Depends(database.get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def create_task(user: User, db: db_dependency): 
    db_user = models.Users(user_name=user.user_name, email=user.email, password=Hash.bcrypt(user.password)) 
    db.add(db_user)
    db.commit() 
    db.refresh(db_user) 
    return db_user

