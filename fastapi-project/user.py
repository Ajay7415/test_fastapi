from fastapi import APIRouter#, Annotated
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix = "/user", tags = ['user'])

class User(BaseModel):
    username:  str 
    first_name  : str 
    last_name : str
    mobile  : int= None 



user_data  = {1 :{"username": "test776", "first_name": "test" ,  "last_name": "user" , "mobile": 7415496606}}

@router.get('/{user_id}')
async def get_user(user_id:int, name: str=None):
    user = user_data.get(user_id, None) 
    return user if user else {"message": "user not found "}


@router.post("/add_user/")
async def add_user(user: User=...): 
    id = max(user_data.keys())
    user_data[id]= user
    return {"message": "User added successfully", "data" : user_data[id]}

@router.put("/update_user/{user_id}")
async def update_user(user_id:int, user:User=...):
    user_in_data  = user_data.get(user_id, None)
    if not user_in_data:
        return {"message": "user not found "}
    user_data[user_id] = user
    return {"message": "user updated successfully", "data": user_data[user_id]}