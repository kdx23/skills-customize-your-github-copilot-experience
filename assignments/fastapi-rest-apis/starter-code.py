"""Starter code for the FastAPI REST APIs assignment.

Run locally with:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Student Item API")


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)


items = []


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}


@app.get("/items")
def list_items():
    # TODO: Return all items in the in-memory list.
    return items


@app.post("/items")
def create_item(payload: ItemCreate):
    # TODO: Convert the validated payload to a dict and store it in items.
    # TODO: Return a response containing a success message and the new item.
    return {"message": "Implement POST /items", "item": payload.model_dump()}
