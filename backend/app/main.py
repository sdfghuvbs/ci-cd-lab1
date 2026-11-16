from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy import select
from .db import SessionLocal
from .models import Item
app = FastAPI(title="CICD Lab 4 Items API")
class ItemInput(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str = Field(default="", max_length=500)
class ItemOut(ItemInput):
    id: int
    model_config = {"from_attributes": True}
def get_db():
    with SessionLocal() as db:
        yield db
@app.get("/api/health")
def health():
    return {"status": "ok"}
@app.get("/api/items", response_model=list[ItemOut])
def list_items(db: Session = Depends(get_db)):
    return db.scalars(select(Item).order_by(Item.id)).all()
@app.post("/api/items", response_model=ItemOut, status_code=201)
def add_item(data: ItemInput, db: Session = Depends(get_db)):
    obj = Item(**data.model_dump()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.put("/api/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, data: ItemInput, db: Session = Depends(get_db)):
    obj = db.get(Item, item_id)
    if not obj: raise HTTPException(404, "Item not found")
    for k,v in data.model_dump().items(): setattr(obj,k,v)
    db.commit(); db.refresh(obj); return obj
@app.delete("/api/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    obj = db.get(Item, item_id)
    if not obj: raise HTTPException(404, "Item not found")
    db.delete(obj); db.commit()
