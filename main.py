from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_config import Base, engine, get_db
from models import Person, PersonType
import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/persons/", response_model=list[schemas.Person])
def get_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()

@app.post("/persons/", response_model=schemas.Person)
def create_person(person: schemas.PersonBase, db: Session = Depends(get_db)):
    new_person = Person(**person.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

@app.post("/persontypes/", response_model=schemas.PersonType)
def create_person_type(person_type: schemas.PersonType, db: Session = Depends(get_db)):
    new_type = PersonType(**person_type.dict())
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type
