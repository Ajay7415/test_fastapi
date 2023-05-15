from fastapi import APIRouter, Query, Path
from datetime import datetime
from pydantic import BaseModel
from typing_extensions import Annotated
from typing import List

# router = APIRouter(prefix = "/user", tags = ['user'])

# class User(BaseModel):
#     username:  str 
#     first_name  : str 
#     last_name : str
#     mobile  : int= None 

# user_data  = {1 :{"username": "test776", "first_name": "test" ,  "last_name": "user" , "mobile": 7415496606}}

# # --------------------------------------------------#
# # ------Api with Operations in query params---------#
# # --------------------------------------------------#

# '''
# ----------------------------------QUICK TIP------------------------------------
# 1. WE CAN ALSO ADD A PARMETER CALL REQUERED AFTER = IN ANNOTATED TO MAKE FIELD REQUIRED FOR EG.
# from pydantic import Required
# async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
# alias in query used to provide query alias in params
# '''

# @router.get('/search_user')
# async def search_user_with_query_params(q: str=Query( default='a', min_length=1, max_length =200)):  # or we can use default values in Annotated level like :-- q: Annotated[str,  Query()] = None
#     return { "message": ["ajay", "arun", "abhay", "anand",  "aman", "akshay", "akash"]}


# # PASSIGN MULTIPLE QUERYPARAMS AS A LIST 
# @router.get('/search_user_list')
# async def search_user_with_query_params_multi_value(q: Annotated[List[str], Query()]= ['ajay', 'mani']):  # or we can use default values in Annotated level like :-- q: Annotated[str,  Query()] = None
#     return { "message": ["ajay", "arun","mani"]}


# # --------------------------------------------------#
# # ------Api with ----Operations---- in Path---------#
# # --------------------------------------------------#

# @router.get('/user_id/{user_id}')
# async  def  get_user_detail(user_id: Annotated[int,  Path(title="Id used to get the detail of a user", gt=0, le=1000)], q:Annotated[str,  Query(min_length=1, max_lenght =200)]= None):
#     return user_data[user_id] if user_data.get(user_id) else {"message": "user not found    "}

# # --------------------------------------------------#
# # ------ API TO PERFORM --- CRUD OPERATION ---------#
# # --------------------------------------------------#

# @router.get('/{user_id}')
# async def get_user(user_id:int, name: str=None):
#     user = user_data.get(user_id, None) 
#     return user if user else {"message": "user not found "}


# @router.post("/add_user/")
# async def add_user(user: User=...): 
#     id = max(user_data.keys())
#     user_data[id]= user
#     return {"message": "User added successfully", "data" : user_data[id]}

# @router.put("/update_user/{user_id}")
# async def update_user(user_id:int, user:User=...):
#     user_in_data  = user_data.get(user_id, None)
#     if not user_in_data:
#         return {"message": "user not found "}
#     user_data[user_id] = user
#     return {"message": "user updated successfully", "data": user_data[user_id]}


from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

import crud, models, schema 
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

router = APIRouter( tags = ['user'])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schema.Item)
def create_item_for_user(
    user_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items