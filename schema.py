from pydantic import BaseModel, Field
from typing import Optional, List

# create your data schema here

class UserSignupRequest(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str
 
 
class UserSigninRequest(BaseModel):
    email: str
    password: str  