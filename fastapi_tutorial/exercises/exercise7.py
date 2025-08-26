from fastapi import FastAPI , Form , File , UploadFile

app = FastAPI()

@app.post("/register/")
def register_user(username : str = Form(...) , email : str = Form(...) , password : str = Form(...)):
    return{
        "username" : username,
        "email" : email,
        "password" : password
    }


@app.post("/upload-resume")
async def upload_resume(file : UploadFile = File(...)):
    # file_content = await file.read()
    return{
        "filename" : file.filename,
        "type" : file.content_type
    } 

@app.post("/submit-application/")
async def submit(name : str = Form(...) , position : str = Form(...) , file : UploadFile= File(...)):

    return{
        "name" : name,
        "position" : position,
        "filename" : file.filename
    }