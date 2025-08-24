from fastapi import FastAPI

app = FastAPI()

detail = {
  "name": "Rishi",
  "age": 23,
  "favorite_language": "Python"
}


@app.get("/info")
def name():
    return detail

@app.get("/square/{num}")
def square(num : int):
    return {"number": num , "square" : num **2}

