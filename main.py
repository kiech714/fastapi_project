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
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

@app.post("/person-types/", response_model=schemas.PersonType)
def create_person_type(person_type: schemas.PersonTypeBase, db: Session = Depends(get_db)):
    db_type = PersonType(**person_type.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

@app.get("/person-types/", response_model=list[schemas.PersonType])
def get_person_types(db: Session = Depends(get_db)):
    return db.query(PersonType).all()
