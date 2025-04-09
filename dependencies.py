from typing import Annotated
from sqlalchemy.orm import Session

# create your dependencies here

def get_db():
    db = None
    try:
        db = Session()
        print("Database connection established")
        yield db
    except Exception as e:
        print("Error connecting to the database:", e)
        db.close()