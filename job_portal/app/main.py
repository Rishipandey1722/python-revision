from fastapi import FastAPI 
from routes import job_routes


applications = []


app = FastAPI()
app.include_router(job_routes.router)



