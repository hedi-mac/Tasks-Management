from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from datetime import datetime, timedelta
import repository.user

def get_all(
    db,
    page: int,
    per_page: int,
    finished: bool,
    created_at_start: datetime,
    created_at_end: datetime,
    finished_at_start: datetime,
    finished_at_end: datetime,
):
    offset = (page - 1) * per_page
    query = db.query(models.Tasks)
    if finished is not None:
        query = query.filter(models.Tasks.finished == finished)
    if created_at_start:
        query = query.filter(models.Tasks.created_at >= created_at_start)
    if created_at_end:
        query = query.filter(models.Tasks.created_at <= created_at_end)
    if finished_at_start:
        query = query.filter(models.Tasks.finished_at >= finished_at_start)
    if finished_at_end:
        query = query.filter(models.Tasks.finished_at <= finished_at_end)
    tasks = query.offset(offset).limit(per_page).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='no tasks')
    return tasks

def get_by_id(id: int, db):
    result = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    return result

def set_finished(id: int, db, email: str):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    if task.finished : 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='task is done ! status can\'t be changed')
    actual_user = repository.user.get_by_email(email, db)
    task.user_id = actual_user.id
    task.update_status(True)
    db.commit()
    db.refresh(task)
    return {'data': task}

def update(id: int, new_task: schemas.Task, db, email: str):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    if new_task.finished != task.finished :  
        task.update_status(new_task.finished)

        if task.finished : 
            actual_user = repository.user.get_by_email(email, db)
            task.user_id = actual_user.id
    if new_task.title is not None : 
        task.title = new_task.title
    if new_task.description is not None : 
        task.description = new_task.description
    db.commit()
    db.refresh(task)
    return {'data': task}

def create(task: schemas.TaskBase, db): 
    db_task = models.Tasks(title=task.title, description=task.description) 
    db.add(db_task)
    db.commit() 
    db.refresh(db_task) 
    return db_task

def delete(id: int, db):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    db.query(models.Tasks).filter(models.Tasks.id == id).delete(synchronize_session=False)
    db.commit()
    return {'message': 'done'}
