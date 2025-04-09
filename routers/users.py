from fastapi import APIRouter
from passlib.context import CryptContext


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get('/')
def users():
    return {"message": "Hello from the users router!"}