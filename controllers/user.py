# Python
from typing import List
from uuid import UUID
import json

# FastAPI
from fastapi import APIRouter, status, HTTPException, Path, Body

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
        - any
    
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
def show_a_user(
    user_id: UUID = Path(...)
):
    """
    This path operation shows a user in the app

    Parameters:
        - Path parameter:
            - user_id: UUID
    
    Returns a user in the app as a json, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        for user in results:
            if user['user_id'] == str(user_id):
                return user
        
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )

### Delete a user
@router.delete(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User"
)
def delete_a_user(
    user_id: UUID = Path(...)
):
    """
    This path operation delete a user from the app

    Parameters:
        - Path parameter:
            - user_id: UUID
    
    Returns the user that has been deleted form the app as a json, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r', encoding="utf-8") as f:
        results = json.loads(f.read())

        for user in results:
            if user['user_id'] == str(user_id):
                results.remove(user)

                with open('users.json', 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                
                return user
        
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )

### Update a user
@router.put(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User"
)
def update_a_user(
    user_id: UUID = Path(...),
    user_updated: User = Body(...)
):
    """
    This path operation update a user information in the app
    * This path operation do not update the password of the user
    
    Parameters:
        - Path parameter:
            - user_id: UUID
        - Request Body Parameter
            - user_updated: User
    
    Returns the user that has been updated in the app as a json, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        for user in results:
            if user['user_id'] == str(user_id):
                
                user_updated = user_updated.dict()

                # Updating the information
                user['email'] = user_updated['email']
                user['first_name'] = user_updated['first_name']
                user['last_name'] = user_updated['last_name']
                user['birth_date'] = str(user_updated['birth_date'])
                
                # Saving the changes
                with open('users.json', 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                
                return user
            
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
