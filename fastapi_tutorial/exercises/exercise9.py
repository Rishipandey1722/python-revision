from fastapi import  Query , Path , APIRouter , Form , UploadFile , File
from pydantic import BaseModel
# endpoints to practise.

router = APIRouter(
    prefix = "/exercise9"
)

#1 . Book Search (Query parameters)
@router.get("/books/search") 
def get_book_by_id(limit : int = Query(10) , q : str = None ):

    #db logic or any other specific logic..
    return {"q":q , "limit" : limit} 


#2. Get Weather by City (Path parameter)
@router.get("/weather/{city}")
def get_weather_by_city(city : str):
    # add logic for fetching weather details by city
    return {"weather" : "weather is cloudy and rainy ..", "city" : city}


#3. Create Feedback (JSON body)

class Feedback(BaseModel):
    username : str
    rating : int
    comment : str

@router.post("/feedback")
def create_feedback(feedback : Feedback):
    print(feedback)
    return {"message" : "feedback received with id...."}


#4. Upload Profile Picture (Form + File)

@router.post("/profile/upload")
def get_profile_details(username : str = Form(...) ,  file : UploadFile = File(...)):
    return {"message" : "profile uploaded successfully..."}
    

#5. Movie Ratings Filter (Path + Query mix)

@router.get("/movies/{genre}")
def get_movies(genre : str , min_rating  : int):
    return {"genre" : genre , "min_rating" : min_rating}