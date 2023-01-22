# Python
from uuid import UUID
from datetime import date
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI, status

# Models
from models import UserBase, UserLogin, User, Tweet

# Path operations 

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

## AUTHENTICATION

@app.post(
    path="/auth/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=['Authentication']
)
def auth_signup():
    pass

@app.post(
    path="/auth/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=['Authentication']
)
def auth_login():
    pass

## USERS
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=['Users']
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=['Users']
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=['Users']
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=['Users']
)
def update_a_user():
    pass



## Tweets