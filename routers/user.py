from typing import List, Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import User, ShowUser
import database
from repository import user

router = APIRouter(
    prefix="/users",
    tags=['USERS']
)

db_dependency = Annotated[Session, Depends(database.get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
async def create_task(new_user: User, db: db_dependency): 
    return user.create(new_user, db)

