from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, SessionLocal


app=FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@app.post('/todos')
async def create_todo(todo: Todos, db: db_dependency):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo