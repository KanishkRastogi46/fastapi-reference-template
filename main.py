import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from db import Base, engine

load_dotenv()

# create the database tables and establish a connection
Base.metadata.create_all(bind=engine)
from dependencies import get_db

app = FastAPI()

# adding static files and templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# adding api routers
from routers import users
app.include_router(users.router, prefix="/users", tags=["users"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", context={'request':request})

@app.get("/hello/{name}")
def index(request: Request, name: str, q: str = None):
    print(request.headers)
    if name == "":
        return {"message": "Hello World!"}
    if q:
        return {"message": f"Hello {name}!", "query": q}
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8000, reload=True)
    get_db()