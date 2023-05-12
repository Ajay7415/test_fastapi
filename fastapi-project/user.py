from fastapi import APIRouter, Query
from datetime import datetime
from pydantic import BaseModel
from typing_extensions import Annotated
from typing import List

router = APIRouter(prefix = "/user", tags = ['user'])

class User(BaseModel):
    username:  str 
    first_name  : str 
    last_name : str
    mobile  : int= None 

user_data  = {1 :{"username": "test776", "first_name": "test" ,  "last_name": "user" , "mobile": 7415496606}}

# --------------------------------------------------#
# ------Api with Operations in query params---------#
# --------------------------------------------------#


'''
----------------------------------QUICK TIP------------------------------------
1. WE CAN ALSO ADD A PARMETER CALL REQUERED AFTER = IN ANNOTATED TO MAKE FIELD REQUIRED FOR EG.
from pydantic import Required
async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
'''

@router.get('/search_user')
async def search_user_with_query_params(q: str=Query( default='a', min_length=1, max_length =200)):  # or we can use default values in Annotated level like :-- q: Annotated[str,  Query()] = None
    return { "message": ["ajay", "arun", "abhay", "anand",  "aman", "akshay", "akash"]}


# PASSIGN MULTIPLE QUERYPARAMS AS A LIST 
@router.get('/search_user_list')
async def search_user_with_query_params_multi_value(q: Annotated[List[str], Query()]= ['ajay', 'mani']):  # or we can use default values in Annotated level like :-- q: Annotated[str,  Query()] = None
    return { "message": ["ajay", "arun","mani"]}
# --------------------------------------------------#
# ------ API TO PERFORM --- CRUD OPERATION ---------#
# --------------------------------------------------#

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




