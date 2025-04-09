from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def users():
    return {"message": "Hello from the users router!"}