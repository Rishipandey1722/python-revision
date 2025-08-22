from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import status
from fastapi.responses import HTMLResponse , PlainTextResponse , FileResponse , JSONResponse

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




#query param 21/08/2025

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



#22/08/2025 Response Handling


class Book(BaseModel):
    
    title : str
    author : str
    pages : int

@app.post("/book/" , response_model = Book)  
def create_book(book : Book):
    return book


# custom status code

@app.get("/register/" , status_code = status.HTTP_201_CREATED)
def register_user():
    return {"message" : "user registered successfully !!"}


# Returning Other Types (HTML, Plain Text, File)

@app.get("/html/" , response_class = HTMLResponse)
def get_html():
    return "<h1> hello im html..</h1>"


@app.get("/text" , response_class=PlainTextResponse)
def get_text():
    return "I'm plain text ..."

@app.get("/file" , response_class = FileResponse)
def get_file():
    return FileResponse("exercise1.py")



# response with json response more controllable


@app.get("/custom_json")
def custom_json():
    return JSONResponse(
        content =  {"msg": "Custom json response"},
        status_code = 200
    )