from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

class TaskBase(BaseModel):
    title : str
    description : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/tasks")
async def create_tasks(task: TaskBase, db: db_dependency): 
    db_task = models.Tasks(title=task.title, description=task.description) 
    db.add(db_task) 
    db.commit() 
    db.refresh(db_task) 

@app.get('/tasks/{id}')
async def about(id: int, db: db_dependency):
    result = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail='task not found')
    return {'data': result}
