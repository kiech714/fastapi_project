from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

class PersonType(Base):
    __tablename__ = "person_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    person_type_id = Column(Integer, ForeignKey("person_type.id"))
    person_type = relationship("PersonType")
