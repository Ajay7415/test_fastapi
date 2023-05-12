from typing import Union, List
from fastapi import FastAPI, Query
from pydantic import BaseModel, Required
from starlette.responses import HTMLResponse  
from enum import Enum
from typing_extensions import Annotated 
import user
class Test(BaseModel):
    name: str
    price : float
    

app = FastAPI()
app.include_router(user.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello, FastAPI!"}

# @app.post("/test/{test_id}")
# async def test_api(test_id:int, q: str = None):
#     return {"api_called" : f"test/{test_id}/", "query_params": q , "message": "api called successfully"}

# @app.put("/test/{test_id}")
# async  def update_test(test_id:int, test_name: str, test_price:float):
#     return {test_id: test_id, test_name: test_name, test_price: test_price}

# @app.post('/test_user')
# async def  create_user(test: Test):
#     return test


# @app.get("/test_user")
# async def tes_items_for_user(q: Union[str, None] = Query(default=None ,max_length = 50)):
#     return {"some data ": "hello ajay", "q": q }


# @app.get("/items/")
# async def read_items(q: Annotated[List[str], Query(min_length=3)]= ['foo', 'bar'] ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# @app.post("update/user")
# def
