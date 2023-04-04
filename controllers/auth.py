# Python
import json

# FastAPI
from fastapi import APIRouter, status, Body, HTTPException

# Models
from models import User, UserRegister, UserLogin

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

## AUTHENTICATION

### Register a user
@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User"
)
def auth_signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation register a user in the app

    Parameters:
        - Request body parameter
            -user : UserRegister
    
    Return a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user



### Login a user
@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User"
)
def auth_login(user: UserLogin = Body(...)):
        """
    Log in

    This path operation log in a user in the app
    * But we are not using Authentication, just checking that
    the user password and email exist.

    Parameters:
        - Request body parameter
            -user : UserLogin
    
    Return a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
        with open("users.json", "r", encoding="utf-8") as f:
            results = json.loads(f.read()) # list of dicts
            user = user.dict()

            for user_db in results:
                if user_db['email'] == user['email'] and user_db['password'] == user['password']:
                    return user_db
            
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Password or email not valid"
            )
