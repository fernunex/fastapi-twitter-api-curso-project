# Python
from typing import List


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
    pass

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
