# app\schemas\user.py
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    id: str  # Assuming you want to manually set the ID
    email: EmailStr
    full_name: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True
