# Python
from typing import List
import json

# FastAPI
from fastapi import APIRouter, status

# Models
from models import User


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

## USERS

### Show all users
@router.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users"
)
def show_all_users():
    """
    This path operation shows all users in the app

    Parameters:
        -
    
    Returns a json list with all users in the app, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read()) # list of dicts
        return results # Fast api can convert this to a json

### Show a user
@router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User"
)
def show_a_user():
    pass

### Delete a user
@router.delete(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User"
)
def delete_a_user():
    pass

### Update a user
@router.put(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User"
)
def update_a_user():
    pass
