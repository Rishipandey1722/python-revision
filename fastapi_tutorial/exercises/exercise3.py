from fastapi import FastAPI , status
from pydantic import BaseModel
from fastapi.responses import FileResponse



app = FastAPI()

class User(BaseModel):
    
    username : str
    email : str
    password : str

class UserPublic(BaseModel):
    username : str
    email : str

@app.post("/users/",response_model = UserPublic , status_code = status.HTTP_201_CREATED)
def create_user(user:User):
    return user


@app.get("/download/" , response_class = FileResponse)
def download_file():
    return FileResponse("exercise1.py")
