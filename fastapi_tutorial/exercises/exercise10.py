from fastapi import APIRouter , Response , Form , File , UploadFile
from typing import Optional
from fastapi.responses import JSONResponse
from pydantic import BaseModel


router = APIRouter(
    prefix = "/exercise10"
)



@router.get("/demo1")
def demo1():
    data = {"message": "Created successfully"}
    return JSONResponse(status_code=201, content=data)

#1. User Age Verification

@router.get("/users/{username}")
def user_age_verification(age:int):
    if age >= 18:
        return JSONResponse(status_code = 200 , content = "age verified")
    return JSONResponse(status_code = 403 , content = "Access denied")


# by using response object
@router.get("/demo2")
def user_age_verification_using_response(age: int , response: Response):
    response.status_code = 200 if age >= 18 else 403
    return "age verified" if age >= 18 else "access denied"



#2. Create Blog Post

class Blog(BaseModel):
    title : str
    content : str
    tags : list[str]

@router.post("/blogs")
def create_blog(blog : Blog):
    if blog.title == "" or blog.content == "" :
        return JSONResponse(status_code = 400 , content = "Incomplete input")

    return JSONResponse(status_code = 200 , content = "done")

#3. Search Movies
@router.get("/movies/search")
def search_movie(q : Optional[str] = None , year : Optional[int] = 0):
    # logic for movie search
    return "no such movie found"

#4. Upload Resume
@router.post("/resume/upload")
def upload_resume(name : str = Form(...) , email : str = Form(...) , file : UploadFile = File(...)):

    if "pdf" in file.content_type:# checked only for pdf
        return JSONResponse(status_code = 200 , content = "valid file and input")
    return JSONResponse(status_code = 400 , content = "Invalid file.")



#5. Order Status

@router.get("/orders/{order_id}")
def order_status(order_id : int , include_items : bool = False):
    if include_items == True: 
        return JSONResponse(status_code = 200 , content = "items included")
    return JSONResponse(status_code =   404 , content = "not found")
