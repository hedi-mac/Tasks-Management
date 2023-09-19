from fastapi import FastAPI, Query, Depends, HTTPException, status
from datetime import datetime, timedelta
from typing import List, Annotated
from database import engine, SessionLocal
from schemas import TaskBase
from sqlalchemy.orm import Session
import models

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/tasks', status_code=status.HTTP_200_OK)
async def get_all_tasks(
    db: db_dependency,
    page: int = Query(default=1, description="Page number, default is 1"),
    per_page: int = Query(default=10, description="Items per page, default is 10"),
    finished: bool = Query(default=None, description="Filter by finished tasks (True/False/None for all)"),
    created_at_start: datetime = Query(default=None, description="Filter tasks created after this date (YYYY-MM-DD)"),
    created_at_end: datetime = Query(default=None, description="Filter tasks created before this date (YYYY-MM-DD)"),
    finished_at_start: datetime = Query(default=None, description="Filter tasks finished after this date (YYYY-MM-DD)"),
    finished_at_end: datetime = Query(default=None, description="Filter tasks finished before this date (YYYY-MM-DD)"),
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
    return {'data': tasks}

@app.get('/tasks/{id}', status_code=status.HTTP_200_OK)
async def get_task_by_id(id: int, db: db_dependency):
    result = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    return {'data': result}

@app.put('/tasks/{id}/finished', status_code=status.HTTP_202_ACCEPTED)
async def set_task_finished(id: int, db: db_dependency):
    task = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    task.update_status(True)
    db.commit()
    db.refresh(task)
    return {'data': task}

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_tasks(task: TaskBase, db: db_dependency): 
    db_task = models.Tasks(title=task.title, description=task.description) 
    db.add(db_task)
    db.commit() 
    db.refresh(db_task) 


