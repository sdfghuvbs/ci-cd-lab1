from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Items API", version="1.0.0", description="CRUD API for laboratory work #1")

class ItemInput(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(ge=0)

class Item(ItemInput):
    id: int

items: dict[int, Item] = {}
next_id = 1

@app.get('/api/items', response_model=list[Item])
def list_items():
    return list(items.values())

@app.get('/api/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return items[item_id]

@app.post('/api/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemInput):
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item

@app.put('/api/items/{item_id}', response_model=Item)
def update_item(item_id: int, payload: ItemInput):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    item = Item(id=item_id, **payload.model_dump())
    items[item_id] = item
    return item

@app.delete('/api/items/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    del items[item_id]
