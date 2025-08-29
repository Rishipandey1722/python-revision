from models import Applicant
from fastapi import FastAPI , APIRouter , Query , File , UploadFile , Form

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
def apply_job(id: int,applicant : Applicant = Form(...) ,  file : UploadFile = File(...)):
    print(file)
    return "done"

@router.get("/{id}")
def read_application(id : int):
    pass
