from typing import Annotated
from sqlalchemy.orm import Session
from jwt import encode, decode
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()
# create your dependencies here

def get_db():
    db = Session()
    print("Database connection established")
    try:
        yield db
    except Exception as e:
        print("Error connecting to the database:", e)
        db.close()
        
        
def create_access_token(data: dict, expiry: timedelta | None = None):
    data.update({"exp": datetime.now(timezone.utc) + expiry if expiry else datetime.now(timezone.utc) + timedelta(hours=1)})
    token = encode(payload=data, key=os.getenv("JWT_SECRET"), algorithm="HS256")
    return token