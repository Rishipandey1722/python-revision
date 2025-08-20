from fastapi import FastAPI


app = FastAPI()

#get request
@app.get("/")
def read_root():
    return {"message: Hello ji !!!"}


#get request with path param
@app.get("/items/{item_id}")
def read_id(item_id : int):
    return {"item_id":"Item Id is " + str(item_id) }



#post request
@app.post("/greet")
def greet_user(user :str):
    return {"message" : "Hello, " + user}