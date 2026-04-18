from fastapi import FastAPI
from pydantic import BaseModel
from routes import user
from routes import auth
from db.database import Base, engine


app = FastAPI()


app.include_router(user.router, prefix="/users")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}



Base.metadata.create_all(bind=engine)