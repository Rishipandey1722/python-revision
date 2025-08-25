from fastapi import FastAPI , Query
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    student_name : str
    student_age : int

@app.post("/course/{course_id}/enroll")
def get_course(course_id : int , student : Student , notify : bool = Query(False)):  
    return { "course_id" : course_id , "student" : student , "notify":notify}

class Address(BaseModel):
    city :  str
    pincode : int

class Employee(BaseModel):
    name : str
    role : str
    address : Address


@app.post("/company/{company_id}/employee")
def create_employee(company_id : int , employee : Employee ):
    return { "company_id" : company_id , "employee" : employee}
