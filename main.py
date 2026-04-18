from fastapi import FastAPI
from pydantic import BaseModel
from routes import user, profile
from routes import auth
from db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.include_router(user.router, prefix="/users")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}



Base.metadata.create_all(bind=engine)