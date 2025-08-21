from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#get request
@app.get("/")
def read_root():
    return {"message: Hello ji !!!"}


#get request with path param
@app.get("/items/{item_id}")
def read_id(item_id : int):
    return {"item_id":"Item Id is " + str(item_id) }



#post request
@app.post("/greet")
def greet_user(user :str):
    return {"message" : "Hello, " + user}


#query param

@app.get("/items/")
def get_query_param(item_id : int , q : str = None):
    return {"item_id " : item_id , "query ": q} 

#request body using pydantic


class Address(BaseModel):
    city:str
    country:str

class User(BaseModel):
    name : str
    age : int
    email : Optional[str] = None
    address : Address


@app.post("/users/")
def create_user(user: User):
    return {"username":user.name, "age" : user.age, "email" : user.email}


@app.post("/register/")
def register_user(user: User):
    return user