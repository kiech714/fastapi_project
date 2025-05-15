from pydantic import BaseModel

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    person_type_id: int

class Person(PersonBase):
    id: int
    class Config:
        orm_mode = True
