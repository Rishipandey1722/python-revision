from fastapi import FastAPI , status , HTTPException , Query , APIRouter
from models import Job 
# from main import jobs 

jobs = []

router = APIRouter(

    prefix = "/jobs" ,
    tags=["Jobs"] 
)


# @router.get("/jobs")
# def test():
#     return "JI"



@router.post("/" , response_model = Job , status_code =  status.HTTP_201_CREATED)
def create_job(job : Job):
    job_data = job.model_dump()
    # print(job_data)
    jobs.append(job_data)
    # print(jobs)
    return job



@router.get("/{id}")
def get_job_by_id(id : int):
    
    # print(jobs)
    for job in jobs:
        if job["id"] == id:
            return job
        
    raise HTTPException(status_code=404, detail="Job not found")



@router.get("/" , response_model = list[Job])
def job_filter(q : str | None = Query(None , min_length = 3 , max_length = 20) , limit : int = Query(5 , le = 20)):

    result = []
    if q:
        print(jobs)
        for i in jobs:
            if q.lower() in i["title"].lower():
                print(i)
                result.append(i)
        
        return result[:limit]
    
    raise HTTPException(status_code=404, detail="Job not found")

