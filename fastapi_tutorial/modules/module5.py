#🔹 Module 5: Path & Query Parameters (Advanced) 24/08/2025
from fastapi import FastAPI , Path , Query


app = FastAPI()

#1. Path Parameters with Validation
@app.get("/items/{item_id}") # item_id must be int otherwise 422 error
def get_item(item_id: int):
    return {"item_id" : item_id}


#Path with regex Only accepts alphanumeric usernames (3–10 chars).
@app.get("/users/{username}")
def get_user(username : str = Path(..., regex = "^[a-zA-Z0-9_]{3,10}$")):
    return {"username" : username}



#2. Query Parameters

#Example: Optional query parameter

@app.get("/search")
def search_items(q:str = None):
    return {"query" : q}

#Example: With default value

@app.get("/products")
def list_product(limit : int = 10, skip :int = 0):
    return {"limit" : limit , "skip" : skip}

#4. List Parameters

@app.get("/tags")
def get_tags(tags : list[str] = Query([])):
    return {"tags": tags}



