from pydantic import BaseModel

class PersonType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    person_type_id: int

class Person(PersonBase):
    id: int
    person_type: PersonType

    class Config:
        orm_mode = True
