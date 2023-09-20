from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from hashing import Hash

def create(user: schemas.User, db): 
    result = db.query(models.Users).filter(models.Users.email == user.email).first()
    if result:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='existing email')
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