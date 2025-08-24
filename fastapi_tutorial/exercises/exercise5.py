from fastapi import FastAPI , Query

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id :int):
    return {"user_id" : user_id}


@app.get("/items/search")
def seaech_item(q : str = Query(... , min_length = 2 , max_length = 15) , limit :int = Query(5, le = 20)):
    return {"q": q , "limit": limit}