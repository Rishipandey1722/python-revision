from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title : str
    author: str
    page : int


class Student(BaseModel):
    name : str
    age : int
    marks : dict[str , float]


@app.post("/book/")
def create_book(book : Book):
    return book

@app.post("/student/")
def create_student(student:Student):
    marks = 0
    n = len(student.marks)
    for i in student.marks:
        marks += student.marks[i]
    return {"student_name":student.name , "student_age" :student.age , "average_marks":marks/n }
