from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from hashing import Hash
import re

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$'

def create(user: schemas.User, db): 
    result = db.query(models.Users).filter(models.Users.email == user.email).first()
    if result:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='existing email')
    if not user.user_name.strip():
            raise HTTPException(status_code=400, detail="Username cannot be empty.")
    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters long.")
    if not re.match(EMAIL_REGEX, user.email):
        raise HTTPException(status_code=400, detail="Invalid email format.")
    if not re.match(PASSWORD_REGEX, user.password):
        raise HTTPException(status_code=400, detail="Password must contain both characters and numbers.")
    db_user = models.Users(user_name=user.user_name, email=user.email, password=Hash.bcrypt(user.password)) 
    db.add(db_user)
    db.commit() 
    db.refresh(db_user) 
    return db_user

def get_by_email(email: str, db): 
    result = db.query(models.Users).filter(models.Users.email == email).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    return result