from fastapi import FastAPI
from database import engine
import models
from routers import task, user


app = FastAPI()
models.Base.metadata.create_all(bind = engine)

app.include_router(task.router)
app.include_router(user.router)



