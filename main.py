import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()


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