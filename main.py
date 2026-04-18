from fastapi import FastAPI
from pydantic import BaseModel
from routes import user

app = FastAPI()


app.include_router(user.router, prefix="/users")

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/search")
def search(q: str = ""):
    return {"query": q}


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}