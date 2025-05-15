from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_config import Base, engine, get_db
from models import Person
import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/persons/", response_model=list[schemas.Person])
def get_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()
