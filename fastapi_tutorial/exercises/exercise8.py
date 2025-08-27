from fastapi import FastAPI , Depends , HTTPException , status , Query


app = FastAPI()
#task 1

def common_parameters(q : str | None = None , skip : int = 0 , limit : int = 10):
    return { "q" : q , "skip" : skip , "limit" : limit}


@app.get("/product/")
def read_products(common : dict = Depends(common_parameters)):
    return common


@app.get("/user/")
def read_users(common : dict = Depends(common_parameters)):
    return common



#TASK2


def get_current_user(token : str = Query(...)):
    if token != "secrettoken":
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "Invalid user")
    return {"username" :  "chatgpt"}

@app.get("/profile")
def get_profile(token : str = Depends(get_current_user)):
    return token


#Task 3 – Nested Dependency

def get_db(connection : str = "Fake DB Connection"):
    return connection

def get_repo(db : str = Depends(get_db)):
    return "Repo using "  + db

@app.get("/repo")
def read_repo(repo : str = Depends(get_repo)):
    return repo
