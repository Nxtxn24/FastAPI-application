from fastapi import FastAPI
from pydantic import BaseModel
from routes import user
from db.database import Base, engine

app = FastAPI()


app.include_router(user.router, prefix="/users")

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}



Base.metadata.create_all(bind=engine)