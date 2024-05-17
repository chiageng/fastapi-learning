from fastapi import FastAPI, Depends, HTTPException, Path
import models
from database import engine, SessionLocal, Base
from typing import Annotated
from sqlalchemy.orm import Session
from models import Todos
from starlette import status 
from pydantic import BaseModel, Field
from routers import auth, todos, admin, user
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)