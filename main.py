import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from db import Base, engine

load_dotenv()

# create the database tables and establish a connection
Base.metadata.create_all(bind=engine)
from dependencies import get_db

app = FastAPI()

from routers import users
app.include_router(users.router, prefix="/users", tags=["users"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello/{name}")
def index(request: Request, name: str, q: str = None):
    print(request.headers)
    if name == "":
        return {"message": "Hello World!"}
    if q:
        return {"message": f"Hello {name}!", "query": q}
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run(app=app)
    get_db()