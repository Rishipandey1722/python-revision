from fastapi import FastAPI 
from routes import job_routes , applications_routes


applications = []


app = FastAPI()
app.include_router(job_routes.router)
app.include_router(applications_routes.router)



