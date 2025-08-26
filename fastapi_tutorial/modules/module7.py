#Module 7: Form Data & File Upload

from fastapi import FastAPI , Form , File , UploadFile

app = FastAPI()

#1. Form Data

@app.post("/login/") # use form data , if json used it will send 422 code.
def login(username : str = Form(...) , password : str = Form(...)):
    return {"username" : username , "message" : "login successful.."}


#2. File Upload (Single File)

@app.post("/upload-file")
async def upload_file(file :UploadFile = File(...)):
    content = await file.read()
    return {
        "filename": file.filename,
        "type" : file.content_type,
        "size" : len(content)
    }

#3. Multiple File Uploads
@app.post("/upload-files")
async def upload_multiple_files(files : list[UploadFile] = File(...)):
    return [{"filename" : f.filename } for  f in files]


#4. Mix Form + File (Example: Profile Upload)
@app.post("/profile")
async def create_profile(username : str = Form(...) , age : int = Form(...) , file : UploadFile = File(...)):

    return {
        "username" : username,
        "age" : age,
        "filename" : file.filename
    }