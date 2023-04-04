# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# Users

class UserBase(BaseModel):
    user_id: UUID = Field(
        ...
        )
    email: EmailStr = Field(
        ...
        )    

class UserLogin(UserBase):
    user_id: Optional[UUID] = Field()
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )

class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(
        default=None
        )

class UserRegister(User, UserLogin):
    pass