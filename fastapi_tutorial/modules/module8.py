#📘 Module 8: Path Operation Dependencies
from fastapi import FastAPI , Depends , HTTPException , status

app = FastAPI();


#1. Simple Dependency Example
def common_parameters(q : str | None = None , skip : int = 0 , limit : int = 10):
    return {"q" : q , "skip" : skip , "limit" : limit}

@app.get("/items")
def get_items(commons : dict = Depends(common_parameters)):
    return commons;

# ✅ Depends() tells FastAPI: “Before running the endpoint, run this function and inject its return value.”


@app.get("/users/")
def read_user(commons : dict = Depends(lambda : common_parameters(q = "Spring boot" , skip = 000) )):
    return commons;


#2. Dependency with Authentication

def verify_token(token : str = "secret987"):
    if (token != "secret987"):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "invalid token")
    
    return token


@app.get("/secure-data/")
def secure_data(token : str = Depends(verify_token)):
    return { "message" : "You have access" , "token" : token}


#3. Class as Dependency

class Pagination():
    def __init__(self , skip : int = 0 , limit : int = 10):
        self.skip = skip
        self.limit = limit



@app.get("/products/")
def pagination(pagination : Pagination = Depends()):
    return {"skip" : pagination.skip , "limit" : pagination.limit}