from pydantic import BaseModel
from typing import List, Union
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


class ItemBase(BaseModel):
    title : str
    desciption : Union[str,  None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id : int
    owner : int
    class Config: 
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name : Union[str, None] = None 


class UserCreate(UserBase):
    password : str


class User(UserBase):
    id : int
    is_active : Union[bool, None] = None
    items : List[Item] = []

    class Config:
        orm_mode =  True



SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30