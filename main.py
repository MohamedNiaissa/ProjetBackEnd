from fastapi import FastAPI
from pydantic import BaseModel

# pas de async pour les projets

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.post("/items/")
def create_item(item: Item):
    return item