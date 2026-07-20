from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class item(BaseModel):
    id: int
    model: str
    

items: List[item] = []

#Define CRUD enpoints - GET, POST, PUT, DELETE

#Read
@app.get("/")
def read_root():
    return "Welcome to the inventory management system"
    # return {items.append(123,"asdasd")}

#Read
@app.get("/items")
def list_items():
    return items

#Create
@app.post("/items")
def add_item(item: item):
    items.append(item)
    return item
    
#Update
@app.put("/items/{id}")
def update_item(id: int, updated_item: item):
    for index, item in enumerate(items):
        if item.id == id:
            items[index] = updated_item
            return updated_item
    return {"error": "item not found"} 

@app.delete("/items/{id}")
def delete_item(id: int):
    for index,item in enumerate(items):
        if item.id == id:
            deleted_item = items.pop(index)
    return {"error" : "item not found"}
