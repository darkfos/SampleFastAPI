from fastapi import FastAPI
from models import CreateItems

import uvicorn
import random

#Application
app: FastAPI = FastAPI()

all_items: list = list()

#Endpoint to address '/'
@app.get("/")
def root():
    return {"message": "Hello world!"}

# GET request
@app.get("/items/")
def get_items():
    return all_items

# POST request
@app.post("/items")
def create_item(item: CreateItems):
    id_items = random.randint(1, 10000000)
    all_items.append({"id": id_items, "name": item.name})
    return item

if __name__ == "__main__":
    #Run application
    # Other command to start -> uvicorn main:app --reload | main - python module and app us application.
    uvicorn.run(app=app)