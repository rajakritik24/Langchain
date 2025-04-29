from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Ritik'
    age: Optional[int] = None
    email: EmailStr
    school: str = Field(default='DPS', alias='school_name', description='The school name')

# print(Student(name="John"))
student = {"name": "Ritik", "age": 20, "email": "ritik@gmail.com", "school": "DPS"}
student = {"name": "Ritik", "age": 20, "email": "ritik@gmail.com", "school_name": "DPS Sagar"}
print(Student(**student), type(Student(**student)))

pydantic_student = Student(**student)
print(pydantic_student.model_dump())
print(pydantic_student.model_dump(include={"name", "age"}))
print(pydantic_student.model_dump(exclude={"age"}))
print(pydantic_student.model_dump(exclude_none=True))
print(pydantic_student.model_dump(exclude_unset=True))
print(pydantic_student.model_dump(mode="json"))
print(pydantic_student.model_dump_json())

