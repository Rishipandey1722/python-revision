from pydantic import BaseModel


class Job(BaseModel):
    id: int
    title : str
    description : str
    company : str
    salary : float
    # position : str


class Applicant(BaseModel):
    name : str
    email : str
    contact : int
    skills : list[str]