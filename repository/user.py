from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from hashing import Hash

def create(user: schemas.User, db): 
    db_user = models.Users(user_name=user.user_name, email=user.email, password=Hash.bcrypt(user.password)) 
    db.add(db_user)
    db.commit() 
    db.refresh(db_user) 
    return db_user