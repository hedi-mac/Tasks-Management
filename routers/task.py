from typing import List, Annotated
from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import Task, TaskBase, ShowTask, User
import models, oauth2
import database
from datetime import datetime, timedelta
from repository import task

router = APIRouter(
    prefix="/tasks",
    tags=['TASKS']
)

db_dependency = Annotated[Session, Depends(database.get_db)]
get_db = database.get_db


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowTask)
async def get_task_by_id(id: int, db: db_dependency, current_user: User = Depends(oauth2.get_current_user)):
    return task.get_by_id(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowTask])
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
    return task.get_all(db, page, per_page, finished, created_at_start, created_at_end, finished_at_start, finished_at_end)

@router.put('/{id}/finished', status_code=status.HTTP_202_ACCEPTED)
async def set_task_finished(id: int, db: db_dependency):
    return task.set_finished(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_task(id: int, new_task: Task, db: db_dependency):
    return task.update(id, new_task, db)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(new_task: TaskBase, db: db_dependency): 
    return task.create(new_task, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)   
async def delete_task(id: int, db: db_dependency):
    return task.delete(id, db)
