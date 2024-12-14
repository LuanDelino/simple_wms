from uuid import uuid4
from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    name: str
    password: str
    email: EmailStr


class UserResponseDTO(BaseModel):
    id: uuid4
    name: str
    password: str
    email: EmailStr
