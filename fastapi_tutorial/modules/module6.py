from fastapi import FastAPI , Query
from pydantic import BaseModel

# ✅ Module 6: Path + Query + Request Body 25/08/20253
app = FastAPI()


#1. Path + Query


@app.get("/orders/{order_id}")
def get_order(order_id :int , details : bool = Query(False)):
    return {"order_id" : order_id , "details" : details}


#2. Path + Request Body

class Feedback(BaseModel):
    rating : int
    comment : str

@app.post("/product/{product_id}/feedback")
def product_feedback(product_id : int , feedback : Feedback):
    return {"product_id":product_id, "feedback": feedback}


# 3. Path + Query + Request Body Together
class User(BaseModel):
    name : str
    age : int

@app.post("/register/{role}")
def register_user(
        role :str ,
        user : User  ,
        notify : bool = Query(False)):
    return {"role":role , "user": user , "notify" : notify}


#4. Multiple Request Bodies (Nested Models)

class Address(BaseModel):
    city : str
    pincode : int

class Employee(BaseModel):
    name : str
    department : str
    address : Address


@app.post("/employee/")
def create_employee(emp : Employee):
    return emp




