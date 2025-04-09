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

def get_db():
    db = None
    try:
        db = Session()
        print("Database connection established")
        yield db
    except Exception as e:
        print("Error connecting to the database:", e)
        db.close()

app = FastAPI()

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