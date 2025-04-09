from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from typing import Annotated
from sqlalchemy.orm import Session
from uuid import uuid4

from schema import UserSignupRequest, UserSigninRequest
from db import User
from dependencies import get_db, create_access_token

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(user_data: UserSignupRequest, db: Annotated[Session, Depends(get_db)] = None):
    if user_data.password != user_data.confirm_password:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")
    
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(id= uuid4(), fullname=user_data.name, email=user_data.email, password=hashed_password)
    try:
        db.add(new_user)
        db.commit()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return {
        "message": "User created successfully",
        "status": 201
    }
    
    
@router.post('/signin', status_code=status.HTTP_200_OK)
def signin(user_data: UserSigninRequest, db: Annotated[Session, Depends(get_db)] = None):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not pwd_context.verify(user_data.password, user.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token(data={"user_id": str(user.id)})
    return {
        "message": "User signed in successfully",
        "status": 200,
        "token": token
    }