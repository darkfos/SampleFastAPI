from fastapi import APIRouter
from .schemas import CreateItems

import random

all_items: list = list()


# Create Router for other view
item_router: APIRouter = APIRouter(
    prefix="/items", #Prefix for address
    tags=["Items"] #Tags for documentation
)

# GET request for id
@item_router.get("/{item_id}/")
def get_item_for_id(item_id: int):
    for line in all_items:
        if line["id"] == item_id:
            return line
    else:
        return {"information": "No result for id: {}".format(item_id)}

# GET request
@item_router.get("/")
def get_items():
    return all_items

# POST request
@item_router.post("/")
def create_item(item: CreateItems):
    id_items = random.randint(1, 10000000)
    all_items.append({"id": id_items, "name": item.name})
    return item