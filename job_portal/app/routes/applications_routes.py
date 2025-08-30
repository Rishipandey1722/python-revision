from models import Applicant
from fastapi import FastAPI , APIRouter , Query , File , UploadFile , Form
import json
from  routes.job_routes import jobs

router = APIRouter(
    prefix = "/application"
)

applications = []

"""3. Applications (Modules 3, 6, 7)

POST /applications/

Apply for a job with:

Job ID (Query or Path)

Applicant details (Form or JSON)

Resume file upload (UploadFile)

Returns: confirmation with file name saved.

GET /applications/{app_id}

Fetch application details.

GET /applications/

List all applications for a given job (Query param: job_id)."""

@router.get("/check")
def test():
    print("c")
    return "Checks" 


@router.post("/{id}") # not working
async def apply_job(id: int,applicant : str = Form(...) ,  file : UploadFile = File(...)):
    return {"message" : "Successfully applied ..." , "filename" : file.filename}

@router.get("/{id}")
def read_application(id : int):
    result = []
    for i in jobs:
        if i["id"].equals(id):
            return i
    return "Not found"
