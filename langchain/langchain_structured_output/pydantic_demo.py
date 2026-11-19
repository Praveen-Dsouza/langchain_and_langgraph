from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(default=5, ge=0.0, le=10, description="A decimal value represnting the cgpa of student")

new_student = {"age": 23, "email": "john.doe@example.com", "cgpa": 3.5}

student = Student(**new_student)

student_dict = dict(student)
print(student_dict["age"])

student_json = student.model_dump_json()
print(student_json)
