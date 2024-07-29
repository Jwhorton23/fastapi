from fastapi import FastAPI
from enum import Enum


#Instantiate the app
app = FastAPI()

# Define root route
@app.get("/")
async def root():
    return {"Message":"Hello from root"}

@app.post("/")
async def post():
    return {"Message":"Hello from post route"}

# @app.put("/")
# async def put():
#     return {"Message":"Hello from put route"}

# list users
@app.get("/users")
async def list_items():
    return {"Message":"list items route"}

# Define current user
@app.get("/user/me")
async def get_current_user():
    return {"Message":"This is the current user"}

# Get user id
@app.get("/users/{user_id}")
async def get_user(user_id:str):
    return {"User ID":user_id}

# Class to store food items
class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {
            "food name": food_name,
            "message": "you must eat veggies!"
        }
    
    
    elif food_name.value == "fruits":
        return {
            "food name": food_name, 
            "message": "you must eat fruits!!"
        }

    # Default response
    return {
            "food name": food_name, 
            "message": "You like chocolate milk, so do I!"
        }

fake_items_db = [{"item_name": "food"}, {"item_name": "Bar"}, {"item_name": "Baz"}, ]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
# item_id = item id, q = query, short = indicator for dislpay description (true or false)
async def get_item(item_id:str, q:str | None = None, short:bool = False):
    item = {"item_id":item_id}
    if q: 
        item.update({"q":q})
    if  not short:
        item.update({"description": "Add Item description here."})
    return item

# Takes in required parameters of user_id and item_id
@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short:bool = False):
    item = {"item_id":item_id, "owner_id":user_id}
    if q:
        item.update({"q":q})

    if not short:
        item.update(
            {
                "description": "Add description here..."
            }
        )

    return item