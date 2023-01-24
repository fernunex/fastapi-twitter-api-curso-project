# FastAPI
from fastapi import APIRouter, status

# Models
from models import User

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
def auth_signup():
    pass

### Login a user
@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User"
)
def auth_login():
    pass
